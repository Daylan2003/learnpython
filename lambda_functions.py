#def double(x):
 #   return x * 2

#print(double(5))

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Daylan", "Maharaj"))
age_check = lambda age: True if age >= 18 else False
print(multiply(5, 4))
print(age_check(18))