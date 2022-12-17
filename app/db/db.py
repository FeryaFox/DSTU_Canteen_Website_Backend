import json
import os

class DB:
    def __init__(self):
        with open(f"{os.getcwd()}\\app\\canteen_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.canteen_list = data["canteen_list"]

        self.dishes = data["dishes"]

    def get_canteen_list(self):
        return self.canteen_list

    def get_canteen_info(self, canteen_id):
        if len(self.canteen_list) > canteen_id:
            return self.canteen_list[canteen_id]
        else:
            return []

    def get_all_dishes(self):
        return self.dishes

    def get_dish_by_id(self, dish_id):
        for i in self.dishes:
            if i["id"] == dish_id:
                return i
        return []

    def get_dishes_by_canteen_id(self, canteen_id):
        return_list = []
        for i in self.dishes:
            if i["canteen_id"] == canteen_id:
                return_list.append(i)
        return return_list

    def get_dish_by_dish_and_canteen_id(self, canteen_id, dish_id):
        for i in self.dishes:
            if i["id"] == dish_id and i["canteen_id"] == canteen_id:
                return i
        return []
