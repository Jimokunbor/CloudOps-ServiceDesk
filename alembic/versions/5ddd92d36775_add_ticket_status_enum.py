"""add ticket status enum

Revision ID: 5ddd92d36775
Revises: 52ad5a1d265c
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "5ddd92d36775"
down_revision: Union[str, Sequence[str], None] = "52ad5a1d265c"
branch_labels = None
depends_on = None


ticket_status = sa.Enum(
    "NEW",
    "OPEN",
    "ASSIGNED",
    "PENDING",
    "IN_PROGRESS",
    "RESOLVED",
    "CLOSED",
    name="ticketstatus",
)


def upgrade() -> None:
    ticket_status.create(op.get_bind(), checkfirst=True)

    op.execute(
        """
        ALTER TABLE tickets
        ALTER COLUMN status
        TYPE ticketstatus
        USING status::ticketstatus
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE tickets
        ALTER COLUMN status
        TYPE VARCHAR(20)
        USING status::text
        """
    )

    ticket_status.drop(op.get_bind(), checkfirst=True)