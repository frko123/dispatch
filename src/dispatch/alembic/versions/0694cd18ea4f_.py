"""Adds the ability to track which service was engaged by.

Revision ID: 0694cd18ea4f
Revises: c86be389dc1a
Create Date: 2021-02-25 15:57:55.131626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0694cd18ea4f"
down_revision = "c86be389dc1a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("participant", sa.Column("service_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        None, "participant", "service", ["service_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "participant", type_="foreignkey")
    op.drop_column("participant", "service_id")
    # ### end Alembic commands ###
