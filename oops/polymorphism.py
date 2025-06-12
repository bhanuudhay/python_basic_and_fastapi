class Car:
    total_cars = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel" 


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge" 


my_tesla  = ElectricCar("Tesla","Model S",100)
# print(my_tesla.brand)
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())
print(my_tesla.fuel_type())
safari = Car("Safari","2020")
print(safari.fuel_type())
print(Car.total_cars)