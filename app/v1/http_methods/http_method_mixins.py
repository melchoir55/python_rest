from app.v1.http_methods.http_method import HttpMethod


class GetMixin(HttpMethod):
    child_fields = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, uid=None):
        query = self.class_name.query
        if uid:
            query.filter_by(id=id)
        return self.create_response(
            query.all(),
            self.fields_returnable,
            200
        )