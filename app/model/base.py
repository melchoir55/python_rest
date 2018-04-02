from sqlalchemy import Column, Integer, DateTime, func
from app import db


class BaseResource(db.Model):

    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=func.current_timestamp())
    modified = Column(
        DateTime,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )

    settable_fields = set()  # defines which fields can be set explicitly by the object constructor.

    def __init__(self, **kwargs):
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in self.settable_fields)

    @classmethod
    def get_serialization_schema(cls):
        raise NotImplementedError("This model has not implemented the get_serialization_schema method.")