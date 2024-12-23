"""add migrations

Revision ID: b957f89dd35c
Revises: fc5eadba2202
Create Date: 2024-12-23 08:34:14.442599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b957f89dd35c'
down_revision: Union[str, None] = 'fc5eadba2202'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'wallet', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wallet', type_='unique')
    # ### end Alembic commands ###