import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_get_wallets(test_client):

    response = test_client.get("/api/v1/wallet")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 0
