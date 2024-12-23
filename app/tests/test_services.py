from datetime import datetime, timezone

from models.models import Wallet


def test_wallet_creation(db_session):
    new_wallet = Wallet(
        address="some_address",
        bandwidth=100,
        energy=50,
        trx_balance=10.5,
        created_at=datetime.now(timezone.utc)
    )
    
    db_session.add(new_wallet)
    db_session.commit()
    
    saved_wallet = db_session.query(Wallet).filter_by(address="some_address").first()
    
    assert saved_wallet is not None
    assert saved_wallet.address == "some_address"
    assert saved_wallet.bandwidth == 100
    assert saved_wallet.energy == 50
    assert saved_wallet.trx_balance == 10.5
    assert saved_wallet.created_at is not None
