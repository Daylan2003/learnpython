#Abstract classes prevents the user from creating an object of that class
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("You stop the motorcycle")        

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()