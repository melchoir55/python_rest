from flask_restful import abort
from app.v1.constants import ErrorCodes


def error(status_code, code, url=None, message="Unknown error"):
    """
    Interrupts processing flow in order to return an error to the user.
    :param status_code: The http response code.
    :param code: An internal error code.
    :param url:  A url at which a user can find more information about the error.
    :param message: A message intended for end user consumption.
    :return:
    """

    if not url:
        url = f'/v1/error/{str(code)}'
    error_data = {
        'url': url,
        'message': message
    }
    abort(status_code, code=code, **error_data)


def get_model_or_404(model_class, uid):
    model_instance = model_class.query.filter_by(uid=uid).first()
    if model_instance is None:
        error(404,
              ErrorCodes.RESOURCE_NOT_FOUND,
              message=f'Specified resource not found: {uid}')
    return model_instance
