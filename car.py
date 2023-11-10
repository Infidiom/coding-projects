"""
A class has two main things to not:
    attributes and methods

Attributes are like class, model, year
Methods are like functions used inside of classes
"""


class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
       """Intialize variables to describe this car"""
       self.make = make
       self.model = model
       self.year = year
       self.speedmeter_reading = 0


    def get_full_car_description(self):
        """Returns the full description of the car"""
        full_description = f"{str(self.year)} {self.make} {self.model} model"
        return full_description
 
    def read_speed_meter(self):
         """Prints a message showing the car's speed meter"""
         print(f"This car is running at {self.speedmeter_reading} km/h")

    def increase_speedmeter_reading(self, value):
        """Updates the current value of the speedmeter reading."""
        self.speedmeter_reading += value

    def decrease_speedmeter_reading(self, value):
        """Decrease the speed value of the sppedometer"""
        self.speedmeter_reading -= value 
        
          

new_car = Car("Tesla", "f2", 2023)
print(new_car.get_full_car_description())
new_car.speedmeter_reading = int(input("Give a number: "))
new_car.read_speed_meter()
new_car.increase_speedmeter_reading(40)
new_car.read_speed_meter()
new_car.decrease_speedmeter_reading(20)
new_car.read_speed_meter()
