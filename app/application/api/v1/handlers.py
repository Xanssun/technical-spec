from fastapi import APIRouter, HTTPException, status
from schemas.tron_schema import BaseTronRequestSchema, BaseTronResponseSchema
from services.tron_service import tron_service

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
async def wallet(request: BaseTronRequestSchema) -> BaseTronResponseSchema:
    if not tron_service.tron.is_address(request.address):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"error": "Invalid Tron address"})
    return await tron_service.create_wallet_info(address=request.address)
