class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_tesla  = ElectricCar("Tesla","Model S",100)
# print(my_tesla.brand)
print(my_tesla.get_brand())
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.full_name())
