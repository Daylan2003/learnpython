#rows = int(input("How many rows"))
#columns = int(input("How many columns"))
#symbol = input("Enter a symbol to use")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()
# 
#loop control statements
#while True:
#    name = input("Enter you name: ")
#    if name != "":
#        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)    