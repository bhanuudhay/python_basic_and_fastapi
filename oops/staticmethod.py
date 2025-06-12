class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.brand} {self.__model}"

    @staticmethod # method that is not related to the class or instance So there is no need to pass self
    def general_description():
        return "Hello this is car"
    @property # now it can be accessible as a variable
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_tesla  = ElectricCar("Tesla","Model S",100)

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

my_car = Car("Toyota","Corolla")
#my_car.model = "Camry"
# print(my_car.model)
# print(my_car.general_description())
print(Car.general_description())
 