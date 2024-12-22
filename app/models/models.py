import uuid
from datetime import datetime

from infra.postgres import Base
from sqlalchemy import DECIMAL, Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class Wallet(Base):
    __tablename__ = 'wallet'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    address = Column(String, unique=True, nullable=False)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    trx_balance = Column(DECIMAL)
    created_at = Column(DateTime, default=datetime.utcnow)
