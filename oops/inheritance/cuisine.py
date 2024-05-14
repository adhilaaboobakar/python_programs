class Cuisine:
    name=str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name


class Dish(Cuisine):

    dish_name=str
    ingradients=str
    price=int

    def __init__(self,name,dish_name,ingradients,price):
        super().__init__(name)
        self.dish_name=dish_name
        self.ingradients=ingradients
        self.price=price

        
dish_obj=Dish("Chinese","biriyani","rice,chicken,ginger,onion",200) 
print(dish_obj)
print(dish_obj.price)
