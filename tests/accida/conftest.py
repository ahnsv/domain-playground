from models.accida.base import AccidaBase
import pytest


@pytest.fixture(scope="module")
def base():
    return AccidaBase