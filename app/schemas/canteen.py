from pydantic import BaseModel


class CanteenInfo(BaseModel):
    id: int
    name: str
    description: str
    place: str
    photo: list[str]
