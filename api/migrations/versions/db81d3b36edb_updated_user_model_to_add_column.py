"""Updated user model to add column

Revision ID: db81d3b36edb
Revises: 4a6dadcaeeda
Create Date: 2024-07-01 11:03:31.709673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel 


# revision identifiers, used by Alembic.
revision: str = 'db81d3b36edb'
down_revision: Union[str, None] = '4a6dadcaeeda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString()))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###
