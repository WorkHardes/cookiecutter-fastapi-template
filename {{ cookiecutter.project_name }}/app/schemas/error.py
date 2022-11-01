from pydantic import BaseModel


class Error(BaseModel):
    code: int | None = None
    message: str | None = None
