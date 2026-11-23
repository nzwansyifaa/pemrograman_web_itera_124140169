"""Create the matakuliah table.

Revision ID: 20261112_matakuliah
Revises: 20261112_mahasiswa
"""
from alembic import op
import sqlalchemy as sa

revision = "20261112_matakuliah"
down_revision = "20261112_mahasiswa"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "matakuliah",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("kode_mk", sa.Text(), nullable=False, unique=True),
        sa.Column("nama_mk", sa.Text(), nullable=False),
        sa.Column("sks", sa.Integer(), nullable=False),
        sa.Column("semester", sa.Integer(), nullable=False),
        sa.CheckConstraint("sks > 0", name="ck_matakuliah_sks_positive"),
        sa.CheckConstraint(
            "semester > 0", name="ck_matakuliah_semester_positive"
        ),
    )


def downgrade():
    op.drop_table("matakuliah")
