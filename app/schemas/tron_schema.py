from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class BaseTronRequestSchema(BaseModel):
    address: str


class BaseTronResponseSchema(BaseTronRequestSchema):
    bandwidth: int
    energy: int
    trx_balance: Decimal
    created_at: datetime


class PaginationSchema(BaseModel):
    limit: int = Field(10, ge=1, description="Количество записей на странице")
    offset: int = Field(0, ge=0, description="Смещение для пагинации")
