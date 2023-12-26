
#Non Comparative Sorting
import timeit
import random

def shadow_sort_two(original_list):
    sorted_list = [None] * (max(original_list))
    
    for i in range(len(original_list)):
        print(original_list[i])
        sorted_list[original_list[i]-1] = original_list[i]
        

    return ([value for value in original_list if value is not None])




def time_shadow_sort_two():
    setup_code = """
from __main__ import shadow_sort_two
import random
my_list = [random.randint(1, 100) for _ in range(10)]
    """

    stmt = "shadow_sort_two(my_list.copy())"

    # Measure the time it takes to run quick_sort function
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1000)

    print(f"Average execution time: {execution_time:.12f} seconds")

time_shadow_sort_two()