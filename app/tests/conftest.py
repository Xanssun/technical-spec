import pytest
from application.api.main import create_app
from fastapi.testclient import TestClient
from infra.postgres import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Синхронная фикстура для базы данных SQLite
@pytest.fixture(scope='function')
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    session.close()
    Base.metadata.drop_all(engine)

# Фикстура для создания и получения тестового клиента FastAPI
@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    client = TestClient(app)
    yield client
