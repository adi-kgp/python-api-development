"""add content column to posts table

Revision ID: e5a607c84534
Revises: c10b8a46f975
Create Date: 2024-12-03 22:15:02.034515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5a607c84534'
down_revision: Union[str, None] = 'c10b8a46f975'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
