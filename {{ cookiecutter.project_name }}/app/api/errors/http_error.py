from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.schemas import error


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        content=jsonable_encoder(error.Error(code=exc.status_code, message=exc.detail)),
        status_code=exc.status_code,
    )
