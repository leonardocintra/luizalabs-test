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
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('fb_id', sa.Integer),
        sa.Column('username', sa.String(50)),
        sa.Column('name', sa.String(80)),
        sa.Column('gender', sa.String(80), nullable=False),
        sa.Column('birthday', sa.Date(), nullable=False),
    )


def downgrade():
    op.drop_table('users')
