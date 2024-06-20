import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def generate_random_list(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# List sizes to test
sizes = [100000, 500000, 1000000]

# Measuring the time taken for each size
for size in sizes:
    arr = generate_random_list(size)
    time_taken = measure_sort_time(quick_sort, arr)
    print(f"Time taken to sort list of size {size}: {time_taken:.6f} seconds")
