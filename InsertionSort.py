import random
import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_random_list(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# List sizes to test
sizes = [100000, 500000, 1000000]

# Measuring the time taken for each size
for size in sizes:
    arr = generate_random_list(size)
    time_taken = measure_sort_time(insertion_sort, arr)
    print(f"Time taken to sort list of size {size}: {time_taken:.40f} seconds")