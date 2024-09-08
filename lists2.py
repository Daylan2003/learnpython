food = ["pizza", "potato", "Taco", "spaghetti"]
#print(food[-1])

food.append("ice cream")
food.remove("pizza")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()

for x in food:
    print(x)