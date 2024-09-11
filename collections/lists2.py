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

#2d lists are a list of lists
# 
drink = ['coffee','soda', 'tea']
dinner = ['potato', 'taco', 'pizza']
dessert = ["cake", "icr cream"]

food = [drink, dinner, dessert]

print(food[0][0])