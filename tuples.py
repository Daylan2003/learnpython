#tuple = collection which is ordered and unchangeable, used to group together related data

student = ("Daylan", 20, "male")

print(student.count("Daylan"))
print(student.index("Daylan"))

for x in student:
    print(x)

print(student)    

if "Daylan" in student:
    print("daylan is here")