
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0")
except ValueError as e:
    print("Enter only numbers please")
    print(e)    
except Exception as e:
    print(e)
    print("something went wrong :_(")
else:
    print(result)  

finally:
    print("This will always execute")          