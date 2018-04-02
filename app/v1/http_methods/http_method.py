from app.v1.constants import ErrorCodes
from app.v1.utils import error


class HttpMethod:
    @staticmethod
    def create_response(objects, fields, http_code):
        if not objects:
            error(404,
                  ErrorCodes.RESOURCE_NOT_FOUND,
                  message='There were no entities found at this resource')
        result_list = HttpMethod.marshal_objects(objects, fields)
        return HttpMethod.create_envelope(result_list), http_code

    @staticmethod
    def marshal_objects(objects, fields):
        result_list = []
        if isinstance(objects, list):
            for obj in objects:
                schema = obj.get_serialization_schema()
                result_list.append(schema(only=fields).dump(obj).data)
        else:
            schema = objects.get_serialization_schema()
            result_list.append(schema(only=fields).dump(objects).data)
        return result_list

    @staticmethod
    def create_envelope(results=[]):
        return {
            'results_count': len(results),
            'result': results
        }
