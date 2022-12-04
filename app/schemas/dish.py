from pydantic import BaseModel


class DishInfo(BaseModel):
    id: int
    canteen_id: int
    name: str
    category: list[str]
    price: float
