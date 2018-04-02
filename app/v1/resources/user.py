from flask_restful import Resource
from app.model.user import User
from app.v1.http_methods.http_method_mixins import GetMixin


class UserResource(Resource, GetMixin):
    class_name = User
    fields_returnable = {'created', 'email'}

    def get(self, uid=None):
        return super().get(uid)
