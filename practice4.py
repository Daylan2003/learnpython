#lists
"""my_list = [1, 7, 5, 4, 3, 2]
print(len(my_list))

#lists are mutable. We can modify the values in lists
#We can mix and match types in lists

print(my_list[1])
print(my_list[2])
print(my_list[0])

if 2 in my_list:
    print("2 is in the list")

if 4 not in my_list:
    print("4 is not in the list")
else:
    print("4 is in the list")"""        

#list functions

"""my_list = [1,2,3,4,5]

print(sum(my_list))
print(max(my_list))
print(min(my_list))


#sum
counter = 0
for i in my_list:
    counter += i
print(counter)


min = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] < min:
        min = my_list[i]
print(min)"""


"""my_list = [1,2,3,4,5,3]

#my_list.append(4)
#print(my_list)

#my_list.pop(0)
#print(my_list)
#n = 2
#for i in range(n):
#    my_list.pop()
#print(my_list)    

target = 3
i = 0
while True:
    if my_list[i] == target:
        print(i)
        break
    else:
        i += 1"""


#Tuples are very similar to lists but they have one key difference. They are immutable. This means once a tuple has been created it cannot be changed. We create a tuple using paranthesis

#my_tuple = (4,5,6)

#print(my_tuple[0])
#we can still call sum, min and max functions on a tuple since these functions don't modify it

#name = "Daylan"
#age = 20

#tuple_pair = (name, age)
#print(tuple_pair)

#In python a set is similar to a list but with a few key differences. A set is unordered. A set can only contain unique elements

#my_set = {1,2,3}
#print(my_set)
#my_set = {3,2,1}
#print(my_set)

#my_list = [1,2,3,4,5,6,7,1,2,3,4,5,5,5]

'''my_set = set()  #TO declare an empty set
for i in my_list:
    my_set.add(i)

print(my_set) 

my_set.remove(5)
print(my_set)'''

#my_set = set(my_list)
#new_list = list(my_set)
#print(new_list)

#DICTIONARIES
#They store key-vlue pairs.
#The first column is the key and the second column is the value

#name_age = {'Alice':25,
#             'Bob':30,
#            'Charile':35}

#In other programming languages dictionaries are sometimes called maps or hashmaps

#print(name_age) #This prints the dictionary
#print(name_age.items()) #This creates a list of tuples of the key-value pair

#my_dict = {}
#my_dict['Daylan'] = 20
#print(my_dict)

'''my_list = ['Daylan', 'Mommy', 'Daddy', 'Carla']


new_dictionary = {}
for i in range(len(my_list)):
    new_dictionary[my_list[i]] = i

print(new_dictionary)'''  

#dictionaries can't contain duplicate keys. They are like sets in that way.

#my_dict = {'a':1, 'b':2, 'c':3}

#my_dict['a'] = 4
#print(my_dict['a'])

#The keys in a dictionary have to be unique but the values can be duplicated

#for key in my_dict:
#    value = my_dict[key]
#    print(key, value)

'''my_list = [1,2,3,1,2,3,1,2,3]
my_dict = {}

for i in my_list:
    if i not in my_dict.keys():
        my_dict[i] = 0
    my_dict[i] = my_dict[i] + 1

print(my_dict)'''  

name_age = {'Alice':25,
            'Bob':30,
            'Charile':35}

name_age['Daylan'] = 20

print(name_age)

my_set = {1,2,3,4,4}
print(len(my_set))


