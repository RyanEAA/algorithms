import timeit

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def time_quicksort():
    setup_code = """
from __main__ import quick_sort
import random
my_list = [random.randint(1, 100) for _ in range(50)]
    """

    stmt = "quick_sort(my_list.copy())"

    # Measure the time it takes to run quick_sort function
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1000)

    print(f"Average execution time: {execution_time:.6f} seconds")

# Call the function to measure the time
time_quicksort()