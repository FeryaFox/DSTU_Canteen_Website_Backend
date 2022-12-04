from pydantic import BaseModel, FileUrl, HttpUrl


class Error404(BaseModel):
    status_code: int = 404
    text: str
