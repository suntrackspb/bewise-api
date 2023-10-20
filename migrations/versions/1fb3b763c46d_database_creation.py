"""Database creation

Revision ID: 1fb3b763c46d
Revises: 
Create Date: 2023-10-20 18:12:45.584752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1fb3b763c46d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('question', sa.String(length=500), nullable=False),
                    sa.Column('answer', sa.String(length=500), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    # ### end Alembic commands ###
