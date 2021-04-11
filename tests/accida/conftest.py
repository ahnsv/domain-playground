from models.accida.model.entity import AccidaModel
from models.accida.user.entity import User
from models.accida.base import AccidaBase
import pytest


@pytest.fixture(scope="module")
def base():
    return AccidaBase


@pytest.fixture(scope="module")
def accida_session(db_session):
    user1 = User(name="test", hashed_pw="user")
    user2 = User(name="test2", hashed_pw="user")

    accida_default_model = AccidaModel(name="accida", version="v2.0.0")

    db_session.add_all([user1, user2, accida_default_model])
    db_session.commit()

    yield db_session
