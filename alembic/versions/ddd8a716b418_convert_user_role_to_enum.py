"""convert user role to enum

Revision ID: ddd8a716b418
Revises: a425be7097c5
Create Date: 2026-08-11 22:23:47.052966

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "ddd8a716b418"
down_revision: Union[str, Sequence[str], None] = "a425be7097c5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


userrole = postgresql.ENUM(
    "USER",
    "TECHNICIAN",
    "MANAGER",
    "ADMIN",
    name="userrole",
    create_type=False,
)


def upgrade() -> None:
    userrole.create(op.get_bind(), checkfirst=True)

    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN role
        TYPE userrole
        USING upper(role)::userrole
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN role
        TYPE VARCHAR(20)
        USING lower(role)
        """
    )

    userrole.drop(op.get_bind(), checkfirst=True)