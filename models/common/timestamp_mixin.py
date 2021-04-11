from datetime import datetime
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime


@declarative_mixin
class TimestampMixin:
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)