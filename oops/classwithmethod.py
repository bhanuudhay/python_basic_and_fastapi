class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self): # this is an instance method 
        return f"{self.brand} {self.model}"

    


my_car = Car("Toyota", "Corolla")
print(my_car.brand) 
print(my_car.model)
print(my_car.full_name())

my_car2 = Car("Ford", "Mustang")
print(my_car2.brand)
print(my_car2.model)

