"""add user table

Revision ID: be911255cf39
Revises: 15e58cdb7165
Create Date: 2025-09-08 03:18:28.906126

"""
from typing import Sequence, Union

from alembic import op
from psycopg import Column
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be911255cf39'
down_revision: Union[str, Sequence[str], None] = '15e58cdb7165'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                     sa.Column('id',sa.Integer(),nullable=False),
                     sa.Column('email',sa.String(),nullable = False),
                     sa.Column('password',sa.String(),nullable=False),
                     sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                               server_default=sa.text('now()'),nullable=False),
                     sa,sa.PrimaryKeyConstraint('id'),
                     sa,sa.UniqueConstraint('email')
                     )
    

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
