import os
import shutil

path = "C:\\Users\\mahar\\Desktop\\File_Folder\\test.txt"

"""if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location doesn't exist")  """
#try:
 #   with open('C:\\Users\\mahar\\Desktop\\File_Folder\\test.tx') as file:
   #     print(file.read())
#except FileNotFoundError:
    #print("That file was not found")    

#print(file.closed)
"""text = "\nHave a nive day !"

with open('C:\\Users\\mahar\\Desktop\\File_Folder\\test.txt', 'a') as file:
    file.write(text)"""

#We can use: copyfile()
#          : copy()
#       and: copy2()

#shutil.copyfile('C:\\Users\\mahar\\Desktop\\File_Folder\\test.txt', 'C:\\Users\\mahar\\Desktop\\File_Folder\\copy.txt') 

path = "C:\\Users\\mahar\\Desktop\\File_Folder\\copy.txt"
destination = "C:\\Users\\mahar\\Desktop\\New_Folder\\test.txt"

"""try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)    
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found") """

"""try:
    os.remove(path)
    os.rmdir(path) #to remove a folder or directory. Will not delete folder that contains files
    shutil.rmtree(path) #Deletes a directory and all files that are contained within it
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You do not have permission to delete that")"""

#modules, A module is a file containing python code. Mau contain functions, classes, etc.           

import messages as msg
from messages import hello,bye

msg.hello()
msg.bye()