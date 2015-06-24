"""create user table

Revision ID: 2cb9ed98e1c
Revises:
Create Date: 2015-06-21 18:47:29.466924

"""

# revision identifiers, used by Alembic.
revision = '2cb9ed98e1c'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('fb_id', sa.Integer, nullable=False),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('gender', sa.String(80)),
        sa.Column('birthday', sa.Date()),
    )


def downgrade():
    op.drop_table('user')
