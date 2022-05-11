"""Add metric2

Revision ID: c0f4b9bc4e01
Revises: ebd7d2403638
Create Date: 2022-05-11 23:13:04.831798

"""
from alembic import op
import clickhouse_sqlalchemy
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0f4b9bc4e01'
down_revision = 'ebd7d2403638'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('statistics', sa.Column('metric2', clickhouse_sqlalchemy.types.common.Int32(), nullable=True, clickhouse_codec=('DoubleDelta', 'ZSTD')))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('statistics', 'metric2')
    # ### end Alembic commands ###
