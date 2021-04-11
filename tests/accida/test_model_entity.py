from models.accida.model.entity import AccidaModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import pytest


def test_accida_next_model_creation(accida_session: Session):
    accida_model = AccidaModel(name="accida", version="v3.0.0")
    accida_session.add(accida_model)
    accida_session.commit()

    assert True


def test_accida_same_version_creation(accida_session: Session):
    with pytest.raises(IntegrityError) as excinfo:
        existing_version_accida_model = AccidaModel(
            name="accida", version="v2.0.0"
        )
        accida_session.add(existing_version_accida_model)
        accida_session.commit()
    assert "UNIQUE constraint failed: models.version" in str(excinfo.value)
