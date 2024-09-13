#string methods
"""
name = "Daylan"

name.islower()
print(len(name))
print(name.upper())
print(name.find("o"))# finds the index
print(name.capitalize())#Capitalizes the first letter of the string
print(name.count("a"))
print(name.replace("a", "o"))
print(name*3)"""

#string slicing
#we can either use the indexing operator of the slice function [start:stop:step]
"""
name = "Daylan Pravir Maharaj"

first_name = name[:6:1]
last_name = name[-7::]
reversed_name = name[::-2]
print(first_name)
print(last_name)
print(reversed_name)

website1 = "www.google.com"
slice = slice()"""

"""strs = ["flower","flow","flight", "fly", "flew"]

prefix = strs[0]

for i in strs[1::]:
    while i[:len(prefix)] != prefix:
        prefix = prefix[:-2]
print(prefix)        

print(strs[2:4])
name = "Daylan"
print(name[:-2])



variable = ""
print(variable)"""

"""needle = "leet"
haystack = "leetcode"


#print(list(needle))

for i in range(len(haystack)):
    for j in range(len(needle)):
        if needle[j] != haystack[i]:
            break
        else:
            print(i)"""

"""name = "Daylan"
if name[-1] == " ":
    name = name[:-1]

print(name) 
counter = 0
start = 1

while name[-(start)] != " ":
    counter += 1
    start += 1
    print(counter)
print("The final count is " + str(counter))  """

"""height = [1,8,6,2,5,4,8,3,7]
max = 0

for i in range(len(height) - 1):
    for j in range(i + 1, len(height)):
        current_vol = (min(height[i], height[j]) * (j-i))
        if current_vol > max:
            max = current_vol
print(max)"""

name = "Daylan"

print(name.find("p"))
print(name[0:3] + name[4:])
print(Counter(name))

