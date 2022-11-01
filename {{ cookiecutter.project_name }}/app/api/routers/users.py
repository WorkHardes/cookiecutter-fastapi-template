from fastapi import APIRouter

router = APIRouter(prefix="/users")


@router.get("/")
def get_users_plug() -> str:
    return "Hello, World!"
