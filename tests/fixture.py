import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker


@pytest.fixture(scope="function")
def connection():
    engine = create_engine(
        url=os.getenv("TEST_DB_URL", "sqlite:///./mem.db"), encoding="utf-8",
        echo=True
    )
    return engine.connect()


@pytest.fixture(scope="function")
def base(declarative_base):
    return declarative_base


@pytest.fixture(scope="function")
def setup_database(connection, base):
    base.metadata.bind = connection
    base.metadata.create_all()

    yield

    base.metadata.drop_all()


@pytest.fixture(scope="function")
def db_session(setup_database, connection):
    transaction = connection.begin()
    yield scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=connection)
    )
    transaction.rollback()
