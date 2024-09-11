mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]    
zeros = [0] * 5 
combined = zeros + letters

numbers = list(range(20))
print(numbers)

chars = list("Hello World")
print(chars)
print(len(chars))

numbers = list(range(20))
print(numbers[::2])