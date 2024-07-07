import uvicorn
import jwt
from datetime import timedelta
from typing import Annotated
from fastapi import FastAPI, Depends , status, HTTPException, Query
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from sqlmodel import Session , select 
from nanoid import generate 

from db import get_session

from config import settings

from models.urls import Urls
from models.users import User
from models.tokens import oauth2_scheme, Token, TokenData, InvalidToken,create_access_token , get_user_by_token


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8000",
   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root ():
    return {'message': "Root Route"}

@app.get('/url-list', status_code=200)
async def get_url (session:Session = Depends(get_session)):
    statement = select(Urls)
    results = session.exec(statement).all()
    return results

@app.get("/sendit")
async def redirect_to_external_url(url: str = Query(...), session: Session = Depends(get_session)):
# The ellipsis (...) is a special value in FastAPI that
    # indicates the parameter is required.
    # It means that the "url" parameter must be present
    # in the request, and its value must not be None.
    
    # Find the long url via the short
    statement = select(Url).where(Url.short_url == url)
    link = session.exec(statement).first()
    
    # Add the https protocol
    long_url = f"https://{link.long_url}"

    return RedirectResponse(long_url)


@app.post('/add-url', status_code=200)
async def add_url(url_data:Urls, user: User = Depends(get_user_by_token), session: Session=Depends(get_session)):
    if user is not None:
        new_url = Urls(**url_data.model_dump())
        new_url.short_url = generate(size=8)
        session.add(new_url)
        session.commit()
        session.refresh(new_url)
        return {'URL Added:', new_url.title}
    else:
        raise settings.CREDENTIALS_EXCEPTION
    
@app.get('/users-current', status_code=200)
async def current_users(current_user: str = Depends(get_user_by_token), session:Session=Depends(get_session)):
    try:
        user= User.lookup_user(current_user.username,session)
    except:
        raise settings.CREDENTIALS_EXCEPTION
    return {"username": user.username, "id": user.id}

@app.post('/add-user')
async def add_user(user_data: User, session: Session = Depends(get_session)):
    new_user = User(**user_data.model_dump())
    new_user.hashed_password = User.hash_password(new_user.hashed_password);
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"User added:", new_user.username}

@app.post("/Login", status_code=200)
async def Login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],session: Session = Depends(get_session)):
    try:
        user = User.lookup_user(form_data.username, session)
    except:
        raise settings.CREDENTIALS_EXCEPTION
    
    is_validated: bool = user.validate_password(form_data.password)
    
    if not is_validated:
        raise settings.CREDENTIALS_EXCEPTION

        
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"username": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get('/logout', status_code=200)
def logout(token: Token = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        invalid_token = InvalidToken(token=token)
        session.add(invalid_token)
        session.commit()
    except:
        raise settings.CREDENTIALS_EXCEPTION
    return {"details:": "Logged out"}


if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)


