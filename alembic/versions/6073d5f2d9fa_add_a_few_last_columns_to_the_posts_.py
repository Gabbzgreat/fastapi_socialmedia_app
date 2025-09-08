"""add a few last columns to the posts ttable

Revision ID: 6073d5f2d9fa
Revises: 5e38e94faa9a
Create Date: 2025-09-08 03:52:59.903526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6073d5f2d9fa'
down_revision: Union[str, Sequence[str], None] = '5e38e94faa9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,
                                    server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
