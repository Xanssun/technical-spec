from typing import List

from fastapi import APIRouter, Depends, status
from schemas.tron_schema import (BaseTronRequestSchema, BaseTronResponseSchema,
                                 PaginationSchema)
from services.tron_service import TronService, get_tron_service

router = APIRouter(
    tags=['tron'],
)

@router.post(
    "/wallet-info/{address}",
    status_code=status.HTTP_200_OK,
    description="Получает ифнормацию о кошельке, а именно: энергию, пропускную способность и баланс trx",
    summary="Получить информацию о кошельке Tron",
    responses={
        status.HTTP_200_OK: {'model': BaseTronResponseSchema},
    },
)
async def wallet(
    request: BaseTronRequestSchema,
    tron_service: TronService = Depends(get_tron_service)
) -> BaseTronResponseSchema:
    return await tron_service.create_wallet_info(address=request.address)


@router.get(
    "/wallet",
    response_model=List[BaseTronResponseSchema],
    status_code=status.HTTP_200_OK,
    summary='Получение списка кошельков',
    description='Возвращает список кошельков'
)
async def get_wallets(
    pagination: PaginationSchema = Depends(),
    tron_service: TronService = Depends(get_tron_service)
) -> BaseTronResponseSchema:
    return await tron_service.get_wallets(pagination=pagination)
