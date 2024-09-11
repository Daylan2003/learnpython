from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(f"CPU count: {cpu_count()}")

    start_time = time.perf_counter()  # Start the timer

    #a = Process(target=counter, args=(500000000,))
    #b = Process(target=counter, args=(500000000,))
    
    #a.start()  # Start process a
    #b.start()  # Start process b
    
    #a.join()  # Wait for process a to finish
    #b.join()  # Wait for process b to finish

    #end_time = time.perf_counter()  # End the timer

    #print(f"Finished in: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()
