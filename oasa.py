class Car:

    colour = None

class Motorcycle:

    colour = None    

def change_colour(vehicle, colour):

    vehicle.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()
motorcycle_1 = Motorcycle()

change_colour(car_1, "red")
change_colour(car_2, "white")
change_colour(car_2, "blue")
change_colour(motorcycle_1, "grey")

print(car_1.colour)
print(car_2.colour)
print(car_3.colour)
print(motorcycle_1.colour)
