from fastapi import APIRouter

from app.api.routers import users


def get_api_router() -> APIRouter:
    api_router = APIRouter(prefix="/api/v1")

    api_router.include_router(
        users.router,
        tags=["Users API"],
    )

    return api_router
