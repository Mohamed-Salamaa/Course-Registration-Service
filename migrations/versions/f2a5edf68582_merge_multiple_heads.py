"""merge multiple heads

Revision ID: f2a5edf68582
Revises: 7d0275035dec, 2d31f22e0030, 7dc16e860cfd
Create Date: 2025-09-28 10:48:43.652388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2a5edf68582'
down_revision = ('7d0275035dec', '2d31f22e0030', '7dc16e860cfd')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
