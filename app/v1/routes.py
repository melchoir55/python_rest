from flask import Blueprint
from flask_restful import Api
from app.v1.resources.user import UserResource

v1_api = Blueprint('v1_api', __name__)

api = Api(v1_api)

api.add_resource(UserResource, '/v1/user/', endpoint='v1_provider_list')
api.add_resource(UserResource, '/v1/user/<int:uid>/', endpoint='v1_provider_detail')
