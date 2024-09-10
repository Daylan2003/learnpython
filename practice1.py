#lists, tuples, sets and dictionaries

#food = ["potato", "taco", "pizza", "sandwich"]
#print(food)
#print(food[0])
#for i in food:
#    print(i)
#food.append("ice cream")
#for i in range(len(food)):
#    print(food[i])

#2d lists
"""
drinks = ["coffe", "soda", "tea"]
dinner = ["pizza", "hamburger", "hot dog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

#print(food[0][1])

for i in range(len(food)):
    for j in range(len(food[i])):
        print(food[i][j])"""

#tuple = This is a group of ordered unchangeable data which is related together
"""
student = ("Daylan", 21, "Maharaj")

#functions for tuples
#write tuple name then .

student.count(21) # This shows how many times a value appears in a tuple
print(student.index("Daylan")) # This shows the index of a particular value in the tuple"""

#sets - A collection which is unordered and unindexed. There are no duplicate values
"""
utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup"}
utensils.add("napkin")
#utensils.remove("knife")
#utensils.clear()

dishes.update(utensils)
dinner_table = utensils.update(dishes)

#We can also check the similarities and differences in sets
#for similarities we use intersection

for x in dishes:
    print(x)"""

#dictionaries = A changeable, unordered collection of unique key:value pairs. They are fast becuase they use hashing. It allows us to access the value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

#print(capitals.keys())
#print(capitals['Russia'])
#print(capitals.get('Germany'))

#for y in capitals:
#    print(y)

#for x in range(len(capitals)):

#print(capitals.items())
#print(capitals.keys()) #prints only the keys
#print(capitals.values()) #prints only the values
#print(capitals.items()) #prints everything

for x,y in capitals.items():
    print(x, y)
for x in capitals.keys():
    print(x)
for x in capitals.values():
    print(x)  

#We can also change dictionaries using the update method
          
capitals.update({'Germany':'Berlin'}) 
capitals.update({'Germany':'Las Vegas'}) # We can also update existing keys with a new value

for x,y in capitals.items():
    print(x, y)

capitals.pop('China') # This will remove the key:value pair
capitals.clear() # This will remove everything 
   

