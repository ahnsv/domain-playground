from enum import Enum
from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Enum as EnumType, Integer, String
from models.accida.base import AccidaBase
from sqlalchemy import Column


class UserRoleEnum(Enum):
    ADMIN = "admin"
    WRITER = "writer"
    VIEWER = "viewer"


class UserRole(AccidaBase):

    __tablename__ = "user_roles"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(EnumType(UserRoleEnum), nullable=False)
    user_id = Column(Integer(), ForeignKey("users.id"))
    user = relationship("User", back_populates="roles")

    def __init__(self, name: str) -> None:
        self.name = name


class User(AccidaBase):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    hashed_pw = Column(String(100), nullable=False)
    roles: List = relationship("UserRole")
    feedbacks: List = relationship("Feedback")

    def __init__(self, name: str, hashed_pw: str) -> None:
        self.name = name
        self.hashed_pw = hashed_pw

    def update_roles(self, next_roles: List[UserRole]):
        # TODO: check equality
        self.roles = next_roles
