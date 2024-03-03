"""Initial migration

Revision ID: 01959c3313f7
Revises: 
Create Date: 2024-03-03 12:18:25.516739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01959c3313f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(100), unique=True, nullable=False),
        sa.Column('password', sa.String(100), nullable=False),
        sa.Column('user_type', sa.String(20), nullable=False),
    )


def downgrade():
    
    op.drop_table('users')
