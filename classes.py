class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "Yackity"

print(MyClass().variable)
print(myobjectx.variable)
print(myobjecty.variable)

class NumberHolder:

    def __init__(self, number):  # Corrected to double underscores
        self.number = number

    def returnNumber(self):
        return self.number

var = NumberHolder(7)
print(var.returnNumber())

      