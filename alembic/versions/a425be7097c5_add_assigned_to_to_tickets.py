"""add assigned_to to tickets

Revision ID: a425be7097c5
Revises: 5ddd92d36775
Create Date: 2026-08-09 22:27:31.022298
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a425be7097c5"
down_revision: Union[str, Sequence[str], None] = "5ddd92d36775"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "tickets",
        sa.Column(
            "assigned_to",
            sa.UUID(),
            nullable=True,
        ),
    )

    op.create_foreign_key(
        "fk_tickets_assigned_to_users",
        "tickets",
        "users",
        ["assigned_to"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_tickets_assigned_to_users",
        "tickets",
        type_="foreignkey",
    )

    op.drop_column(
        "tickets",
        "assigned_to",
    )