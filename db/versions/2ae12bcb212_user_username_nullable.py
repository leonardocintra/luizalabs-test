"""user_username_nullable

Revision ID: 2ae12bcb212
Revises: 2cb9ed98e1c
Create Date: 2015-06-23 10:12:54.228996

"""

# revision identifiers, used by Alembic.
revision = '2ae12bcb212'
down_revision = '2cb9ed98e1c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column(
        'user',
        sa.Column('username', sa.String(50))
    )


def downgrade():
    pass
