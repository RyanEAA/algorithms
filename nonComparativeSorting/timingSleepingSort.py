import threading
import timeit
import time

# Function that sleeps for the given value and prints it
def sleep_sort(value):
    time.sleep(value*0.00001)
    print(value)

# Function that creates threads for each number in the input list and starts them
def sleep_sorting(numbers):
    # Record the start time
    start_time = timeit.default_timer()
    
    # List to store thread objects
    threads = []
    
    # Create and start a thread for each number in the list
    for number in numbers:
        thread = threading.Thread(target=sleep_sort, args=(number,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Record the end time
    end_time = timeit.default_timer()
    
    # Calculate the total time taken to start all threads
    total_time = end_time - start_time
    
    # Print the total time
    print(f"Total time taken to start all threads: {total_time:.6f} seconds")

# Entry point of the program
if __name__ == "__main__":
    # Example list of numbers
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # Call the sleep_sorting function with the example list
    sleep_sorting(my_list)
    
    # Print the original list (note: the list itself is not sorted by sleep sort)
    print(my_list)
