"""Added username column

Revision ID: 4a6dadcaeeda
Revises: e3efd83c7ac8
Create Date: 2024-06-27 12:24:15.492460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '4a6dadcaeeda'
down_revision: Union[str, None] = 'e3efd83c7ac8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
