#Higher order function = It is a function that either accepts a function as an argument or returns a fucntion
"""
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)    
hello(quiet)"""

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))
print((divisor(2))(10))