"""empty message

Revision ID: 7d0275035dec
Revises: 4e7537cb3831
Create Date: 2021-11-23 01:04:24.115530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d0275035dec'
down_revision = '4e7537cb3831'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.alter_column('courses', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('courses', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('courses', 'course_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('courses', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('courses', 'id')
    # ### end Alembic commands ###
