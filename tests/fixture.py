from models.accida.user.entity import User
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker


@pytest.fixture(scope="module")
def connection():
    engine = create_engine(
        url=os.getenv("TEST_DB_URL", "sqlite:///./mem.db"), encoding="utf-8",
        echo=True
    )
    return engine.connect()


@pytest.fixture(scope="module")
def setup_database(connection, base):
    base.metadata.bind = connection
    base.metadata.create_all()

    yield

    base.metadata.drop_all()


@pytest.fixture(scope="module")
def db_session(setup_database, connection):
    transaction = connection.begin()
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=connection)
    )
    user1 = User(name="test", hashed_pw="user")
    user2 = User(name="test2", hashed_pw="user")

    session.add_all([user1, user2])
    session.commit()

    yield session
    transaction.rollback()
