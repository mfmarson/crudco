import uvicorn
import jwt
from typing import Annotated
from fastapi import FastAPI, Depends , status, HTTPException, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session , select 
from datetime import timedelta
from db import engine, get_session

from models.urls import Urls
from models.users import User
from nanoid import generate 
from config import settings
from models.tokens import Token, create_access_token, TokenData, InvalidToken
from services import get_current_user_token, get_user

oauth2_scheme= OAuth2PasswordBearer(tokenUrl="login")



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

def lookup_user(username: str, session: Session = Depends(get_session)):
    return session.query(User).filter(User.username== username).one()

@app.get('/')
async def root ():
    return {'message': "Root Route"}


@app.get('/url-list')
async def get_url (session:Session = Depends(get_session)):
    statement = select(Urls)
    results = session.exec(statement).all()
    return results



@app.post('/add-url')
async def add_url(url: Urls, session: Session = Depends(get_session)):
    new_url = Urls(**url.model_dump())
    new_url.short_url = generate(size=8)
    session.add(new_url)
    session.commit()
    session.refresh(new_url)
    return {'URL Added:', new_url.title}

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
        user = lookup_user(form_data.username, session)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    is_validated: bool = user.validate_password(form_data.password)
    
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"username": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

# @app.get('/logout', status_code=200)
# def logout(token: Token = Depends(oauth2_scheme), session: Session = Depends(get_session)):
#     try:
#         invalid_token = InvalidToken(token=token)
#         session.add(invalid_token)
#         session.commit()
#     except:
#         raise settings.CREDENTIALS_EXCEPTION
#     return {"details:": "Logged out"}


if __name__== '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)


