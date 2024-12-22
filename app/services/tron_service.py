from datetime import datetime
from decimal import Decimal
from typing import List

from core.config import settings
from fastapi import Depends, HTTPException, status
from infra.postgres import get_session
from models.models import Wallet
from schemas.tron_schema import BaseTronResponseSchema, PaginationSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from tronpy import AsyncTron
from tronpy.providers.async_http import AsyncHTTPProvider


class TronService:
    def __init__(self, api_key: str, db_session: AsyncSession):
        provider = AsyncHTTPProvider(api_key=api_key)
        self.tron = AsyncTron(provider=provider)
        self.db_session = db_session


    async def create_wallet_info(self, address: str) -> Wallet:
        if not self.tron.is_address(address):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Tron address")
        
        existing_wallet = await self.db_session.execute(
            select(Wallet).where(Wallet.address == address)
        )
        if existing_wallet.scalar():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wallet already exists")

        account = await self.tron.get_account_resource(address)
        energy_limit = account.get('EnergyLimit', 0)

        trx_balance = await self.tron.get_account_balance(address)
        bandwidth = await self.tron.get_bandwidth(address)

        wallet = Wallet(
            address=address,
            bandwidth=bandwidth,
            energy=energy_limit,
            trx_balance=Decimal(trx_balance),
        )
        self.db_session.add(wallet)
        await self.db_session.commit()
        await self.db_session.refresh(wallet)

        return wallet
    
    async def get_wallets(self, pagination: PaginationSchema)-> List[BaseTronResponseSchema]:
        query = (
            select(Wallet)
            .limit(pagination.limit)
            .offset(pagination.offset)
        )
        result = await self.db_session.execute(query)
        wallets = result.scalars().all()
        return wallets


def get_tron_service(
        db_session: AsyncSession = Depends(get_session),
):
    return TronService(db_session=db_session, api_key=settings.api_key)
