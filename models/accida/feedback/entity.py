from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from models.accida.base import AccidaBase


class Feedback(AccidaBase):

    __tablename__ = "feedbacks"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    user = relationship("User", back_populates="feedbacks")

    def __init__(self, user_id) -> None:
        self.user_id = user_id
