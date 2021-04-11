from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from models.common.timestamp_mixin import TimestampMixin
from models.accida.base import AccidaBase


class Model(TimestampMixin, AccidaBase):
    __tablename__ = "models"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))
    version = Column(String(30), unique=True)
    feedbacks = relationship("Feedback", back_populates="model")

    def __init__(self, name, version) -> None:
        self.name = name
        self.version = version


class AccidaModel(Model):
    __tablename__ = "accida_models"

    id = Column(Integer, ForeignKey("models.id"), primary_key=True)
    __mapper_args__ = {
        "polymorphic_identity": "accida_models",
    }
