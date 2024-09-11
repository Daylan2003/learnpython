"""def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3))"""

#kwargs = parameter that will pack all arguements into a dictionary

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for y in kwargs.items():
        print(y, end=" ")

hello(first="Daylan", middle="Pravir", last="Maharaj")    