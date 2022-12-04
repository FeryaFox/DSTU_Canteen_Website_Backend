
class DB:

    def __init__(self):
        self.canteen_list = [
            {"id": 0, "name": "Столовая 1", "description": "Ну столовка", "place": "Где-то 1", "photo": ["/img/0/0", "/img/0/1", "/img/0/2"]},
            {"id": 1, "name": "Столовая 2", "description": "Ну столовка", "place": "Где-то 2", "photo": ["/img/1/0", "/img/1/1", "/img/1/2"]},
            {"id": 2, "name": "Столовая 3", "description": "Ну столовка", "place": "Где-то 3", "photo": ["/img/2/0", "/img/2/1", "/img/2/2"]}
        ]

        self.dishes = [
            {"id": 0, "canteen_id": 0, "name": "Вода", "category": ["Напитки"], "price": 50.00},
            {"id": 1, "canteen_id": 1, "name": "Вода", "category": ["Напитки"], "price": 50.00},
            {"id": 2, "canteen_id": 2, "name": "Вода", "category": ["Напитки"], "price": 50.00},
            {"id": 3, "canteen_id": 1, "name": "Кола", "category": ["Напитки"], "price": 50.00},
            {"id": 4, "canteen_id": 0, "name": "Вода", "category": ["Напитки"], "price": 50.00},
            {"id": 5, "canteen_id": 2, "name": "Вода", "category": ["Напитки"], "price": 50.00},
            {"id": 6, "canteen_id": 0, "name": "Вода", "category": ["Напитки"], "price": 50.00},
        ]

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
