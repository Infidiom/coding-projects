from car import *

# Inheritance is when a class inherits properties from another class.
# The classthat is created from another class is called the child class.


class ElectricCar(Car):
    """An car that runs on electricity rather than fuel, lower acceleration. """
    
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 70
# A private method / variable can only be called inside the class
    


    def battery_1(self):
        print(f"The battery has a capacity of {self.battery}mAh, it will last for around {self.battery * 60} hours until recharging and has a range of {self.battery * 6} miles")

    def print_make(self):
        self.__print_make()


my_car = ElectricCar("Tesla", "Z15", 2026) #instance of class "ElectricCar."
print(f"The battery is {my_car.battery} mAh")
print(my_car.get_full_car_description())
my_car.battery_1()
my_car.read_speed_meter()
#Add a method that prints the elctric car, battery life.

def print_car_instance(self, val1):
    if isinstance(val1, str):
        print("This is an instance of Car.")


car2 = Car("Benz", "sClass", 2020)

my_car.print_car_instance(car2, my_car)

print(my_car.battery)