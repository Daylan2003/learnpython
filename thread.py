#thread = A flow of execution. Like a separate order of intstructions.
#           However each thread takes a turn running to achieve concurrency
#           GIL = (Global Interpreter Lock),
#           allows only one thread to hold control of the python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#               use multithreading


import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():   
    time.sleep(5)
    print("You finished studying")

x = threading.Thread(target=eat_breakfast) 
x.start()     

y = threading.Thread(target=drink_coffee) 
y.start()  

z = threading.Thread(target=study) 
z.start()  

x.join()
y.join()
z.join()

print (threading.active_count())
print (threading.enumerate())
print (time.perf_counter())

#eat_breakfast()
#drink_coffee()
#study()