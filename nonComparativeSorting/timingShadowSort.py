
#Non Comparative Sorting
import timeit

def shadow_sort(original_list):
    sorted_list = [None] * (len(original_list))

    for i in range(len(original_list)):
        sorted_list[original_list[i]-1] = original_list[i]
        
    return sorted_list


def time_shadow_sort():
    setup_code = """
from __main__ import shadow_sort
my_list = [10,9,8,7,6,5,4,3,2,1]
    """

    stmt = "shadow_sort(my_list.copy())"

    # Measure the time it takes to run quick_sort function
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1000)

    print(f"Average execution time: {execution_time:.12f} seconds")

time_shadow_sort()