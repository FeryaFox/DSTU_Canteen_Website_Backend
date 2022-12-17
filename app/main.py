from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db import DB
from app.schemas import CanteenInfo, Error404, DishInfo
import os

app = FastAPI()
db = DB()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    # await database.connect()
    ...


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    # await database.disconnect()
    ...


@app.get("/api/canteen/", response_model=list[CanteenInfo])
async def canteen_list():
    return db.get_canteen_list()


@app.get(
    "/api/canteen/{canteen_id}",
    response_model=CanteenInfo,
    responses={
        200: {
            "description": "Canteen requested by ID",
        },
        404: {
            "model": CanteenInfo,
            "description": "Canteen not found"
        },
    }
)
async def canteen_info(canteen_id: int):
    if x := db.get_canteen_info(canteen_id):
        return x
    else:
        raise HTTPException(status_code=404, detail=f"Canteen with id {canteen_id} not found")


@app.get(
    "/api/dish/",
    response_model=list[DishInfo],
    responses={
        200: {
            "description": "Get all dishes"
        },
        404: {
            "model": DishInfo,
            "description": "Dish not found with this canteen_id"
        }
    }
)
async def get_all_dishes(canteen_id: int | None = None):
    if canteen_id is None:
        return db.get_all_dishes()
    if x := db.get_dishes_by_canteen_id(canteen_id):
        return x
    raise HTTPException(status_code=404, detail=f"Canteen with id {canteen_id} not found")


@app.get(
    "/api/dish/{dish_id}",
    response_model=DishInfo,
    responses={
        200: {
            "description": "Get dishes by id"
        },
        404: {
            "model": DishInfo,
            "description": "Dish not found"
        }
    }
)
async def get_dish_by_dish_id(dish_id: int, canteen_id: int | None = None):
    if canteen_id is None:
        return db.get_dish_by_id(dish_id)
    print("f")
    if x := db.get_dish_by_dish_and_canteen_id(canteen_id, dish_id):
        return x
    raise HTTPException(status_code=404, detail=f"Dish with id {dish_id} in canteen {canteen_id} not found")


@app.get("/api/img/{can}/{img_info}")
async def main(can: int, img_info: str):
    return FileResponse(f"{os.getcwd()}/app/static/img/canteen_img/{can}/{img_info}.jpg")


@app.get("/img/{info}")
async def get_img(info: str):
    print(f"{os.getcwd()}/app/static/img/{info}")
    return FileResponse(f"{os.getcwd()}/app/static/img/{info}")
