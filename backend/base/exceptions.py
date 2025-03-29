import traceback

from rest_framework.views import exception_handler
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST

from base.constants import ERROR_CODE_MESSAGE_MAPPING
from base.response import Response


def custom_exception_handler(exc, content):
    traceback.print_exc()
    response = exception_handler(exc, content)
    if response is None:
        return Response(
            status=HTTP_500_INTERNAL_SERVER_ERROR,
            message=ERROR_CODE_MESSAGE_MAPPING[HTTP_500_INTERNAL_SERVER_ERROR]
        )

    if response.status_code in list(ERROR_CODE_MESSAGE_MAPPING.keys()):
        return Response(
            status=response.status_code,
            message=ERROR_CODE_MESSAGE_MAPPING[response.status_code],
            content=exc.detail if hasattr(exc, 'detail') and response.status_code == HTTP_400_BAD_REQUEST else None
        )

    return Response(
        status=response.status_code,
        message='An error occurred'
    )

