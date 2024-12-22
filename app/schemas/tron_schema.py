from decimal import Decimal

from pydantic import BaseModel


class BaseTronRequestSchema(BaseModel):
    address: str


class BaseTronResponseSchema(BaseTronRequestSchema):
    bandwidth: int
    energy: int
    trx_balance: Decimal
