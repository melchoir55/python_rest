from app import ma
from app.model.user import User


class UserSerializationSchema(ma.ModelSchema):
    class Meta:
        model = User
