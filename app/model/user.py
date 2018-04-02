from app.model.base import BaseResource
from sqlalchemy import Column, String


class User(BaseResource):
    __tablename__ = 'User'

    email = Column(String)

    settable_fields = {'email'}


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_serialization_schema(cls):
        from app.model.serialization_schemas.user import UserSerializationSchema
        return UserSerializationSchema

    def __repr__(self):
        return f'<User {self.email}>'
