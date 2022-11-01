from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas import error


async def http422_error_handler(
    _: Request,
    __: RequestValidationError | ValidationError,
) -> JSONResponse:
    message = "validation error"
    return JSONResponse(
        content=jsonable_encoder(
            error.Error(code=status.HTTP_422_UNPROCESSABLE_ENTITY, message=message)
        ),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )
