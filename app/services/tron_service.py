from decimal import Decimal

from core.config import settings
from schemas.tron_schema import BaseTronResponseSchema
from tronpy import AsyncTron
from tronpy.providers.async_http import AsyncHTTPProvider


class TronService:
    def __init__(self, api_key: str):
        provider = AsyncHTTPProvider(api_key=api_key)
        self.tron = AsyncTron(provider=provider)

    async def create_wallet_info(self, address: str) -> BaseTronResponseSchema:

        account = await self.tron.get_account_resource(address)
        energy_limit = account.get('EnergyLimit', 0)

        trx_balance = await self.tron.get_account_balance(address)
        bandwidth = await self.tron.get_bandwidth(address)

        return BaseTronResponseSchema(
            address=address,
            bandwidth=bandwidth,
            energy=energy_limit,
            trx_balance=Decimal(trx_balance)
        )


tron_service = TronService(api_key=settings.api_key)
