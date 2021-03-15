"""empty message

Revision ID: cdca3fcfc278
Revises: 0694cd18ea4f
Create Date: 2021-03-15 13:19:08.067579

"""
from alembic import op
import sqlalchemy_utils
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cdca3fcfc278"
down_revision = "0694cd18ea4f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "organization",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        schema="public",
    )
    op.create_index(
        "ix_organization_search_vector",
        "organization",
        ["search_vector"],
        unique=False,
        schema="public",
        postgresql_using="gin",
    )
    op.create_table(
        "project",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("organization_id", sa.Integer(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["public.organization.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="public",
    )
    op.create_index(
        "ix_project_search_vector",
        "project",
        ["search_vector"],
        unique=False,
        schema="public",
        postgresql_using="gin",
    )
    op.create_table(
        "assoc_user_projects",
        sa.Column("dispatch_user_id", sa.Integer(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["dispatch_user_id"],
            ["public.dispatch_user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["public.project.id"],
        ),
        schema="public",
    )
    op.add_column("dispatch_user", sa.Column("organization_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        None,
        "dispatch_user",
        "organization",
        ["organization_id"],
        ["id"],
        source_schema="public",
        referent_schema="public",
    )
    op.drop_constraint("search_filter_creator_id_fkey", "search_filter", type_="foreignkey")
    op.create_foreign_key(
        None, "search_filter", "dispatch_user", ["creator_id"], ["id"], referent_schema="public"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "search_filter", type_="foreignkey")
    op.create_foreign_key(
        "search_filter_creator_id_fkey", "search_filter", "dispatch_user", ["creator_id"], ["id"]
    )
    op.drop_constraint(None, "dispatch_user", schema="public", type_="foreignkey")
    op.drop_column("dispatch_user", "organization_id")
    op.drop_table("assoc_user_projects", schema="public")
    op.drop_index("ix_project_search_vector", table_name="project", schema="public")
    op.drop_table("project", schema="public")
    op.drop_index("ix_organization_search_vector", table_name="organization", schema="public")
    op.drop_table("organization", schema="public")
    # ### end Alembic commands ###
