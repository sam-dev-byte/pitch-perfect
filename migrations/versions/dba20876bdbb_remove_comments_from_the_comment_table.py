"""remove comments from the comment table

Revision ID: dba20876bdbb
Revises: ce171c1203a1
Create Date: 2018-01-09 11:55:02.684557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dba20876bdbb'
down_revision = 'ce171c1203a1'
branch_labels = None
depends_on = None


def upgrade():
        op.drop_column('comments', 'comment_title')
  


def downgrade():
    op.add_column('comments', sa.Column('comment_title', sa.VARCHAR(), autoincrement=False, nullable=True))
   
