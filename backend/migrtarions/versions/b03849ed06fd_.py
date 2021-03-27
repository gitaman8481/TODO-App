"""empty message
Revision ID: b03849ed06fd
Revises: 274b68063340
Create Date: 2019-11-05 11:19:38.581048
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b03849ed06fd'
down_revision = '274b68063340'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'title')
    # ### end Alembic commands ###