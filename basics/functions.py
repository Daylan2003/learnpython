def my_function():
    print("Hello from My Function !")

username = "You"
greeting = "The best"

def my_function_with_arguments(username, greeting):
    print("Hello, %s, from My Function! I wish you %s" % (username, greeting))

# Call the function
my_function_with_arguments(username, greeting) 

def sum_two_numbers(a, b):
    return a + b