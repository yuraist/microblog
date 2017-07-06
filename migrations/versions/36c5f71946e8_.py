"""empty message

Revision ID: 36c5f71946e8
Revises: 
Create Date: 2017-07-03 21:34:15.222928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36c5f71946e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('post_user_id_fkey', 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('post_user_id_fkey', 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###