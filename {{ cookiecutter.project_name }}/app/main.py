from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api.errors import http_error, validation_error
from app.api.routers import api


def get_application() -> FastAPI:
    app = FastAPI(title="Some API")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.add_event_handler("startup", events.some_startup_event)

    # app.add_event_handler("shutdown", events.events.some_shutdown_event)

    app.add_exception_handler(HTTPException, http_error.http_error_handler)
    app.add_exception_handler(
        RequestValidationError, validation_error.http422_error_handler
    )

    api_router = api.get_api_router()
    app.include_router(api_router)

    return app


app = get_application()
