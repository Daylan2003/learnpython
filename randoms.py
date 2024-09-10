import random
import time

x = random.randint(1,6)
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print("Hi")
time.sleep(2)
print("Welcome to Rock Paper Scissiors !")
for i in range(10):
    print("#", end="")