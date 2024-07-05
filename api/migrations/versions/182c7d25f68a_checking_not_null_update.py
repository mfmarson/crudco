"""Checking not null update

Revision ID: 182c7d25f68a
Revises: db81d3b36edb
Create Date: 2024-07-01 11:13:26.210095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '182c7d25f68a'
down_revision: Union[str, None] = 'db81d3b36edb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'hashed_password',
            existing_type=sa.VARCHAR(),
            nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'hashed_password',
            existing_type=sa.VARCHAR(),
            nullable=True)
    # ### end Alembic commands ###