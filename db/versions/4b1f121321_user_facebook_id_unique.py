"""user_facebook_id_username_unique

Revision ID: 4b1f121321
Revises: 2ae12bcb212
Create Date: 2015-06-23 19:21:35.356544

"""

# revision identifiers, used by Alembic.
revision = '4b1f121321'
down_revision = '2ae12bcb212'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column(
        'user',
        sa.Column('facebook_id', sa.String(80), unique=True),
    )


def downgrade():
    pass
