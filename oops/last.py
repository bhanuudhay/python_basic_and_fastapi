class Battery:
    def battery_info(self):
        return "This is a battery"
class Engine:
    def engine_info(self):
        return "This is a engine"

class ElectricCar(Battery,Engine):
    pass

my_new_tesla = ElectricCar()

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
