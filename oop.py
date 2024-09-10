#object oriented programming

class Car:

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")

    pass

car_1 = Car("Chevy", "Corvette", "2021", "blue")
car_2 = Car("Ford", "Mustang", "2022", "Red")
 


car_1.drive()
car_1.stop()



car_2.drive()
car_2.stop()