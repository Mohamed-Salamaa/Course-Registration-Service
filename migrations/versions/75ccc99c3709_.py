"""empty message

Revision ID: 75ccc99c3709
Revises: 1d0989e9f8f0
Create Date: 2021-11-26 17:38:13.796965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ccc99c3709'
down_revision = '1d0989e9f8f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('teacher_name', sa.String(length=200), nullable=False),
    sa.Column('teacher_email', sa.String(length=200), nullable=False),
    sa.Column('teacher_phone', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('price', sa.String(length=150), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    op.drop_table('course')
    op.drop_table('teacher')
    op.drop_table('student')
    # ### end Alembic commands ###