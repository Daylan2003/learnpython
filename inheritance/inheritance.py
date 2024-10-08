class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
    pass

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
    pass

class Hawk(Animal):
    def fly(self):
        print("This hawk is swimming")
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.run()
fish.swim()
hawk.fly()
fish.eat()
hawk.sleep()