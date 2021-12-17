"""empty message

Revision ID: 7dc16e860cfd
Revises: 93f4420ea8cf
Create Date: 2021-12-17 16:27:17.534190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dc16e860cfd'
down_revision = '93f4420ea8cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('public_id', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'public_id')
    # ### end Alembic commands ###