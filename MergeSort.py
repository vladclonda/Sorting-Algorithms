import random
import time

def merge(arr, l, m, r):
    # Create temp arrays
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

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
    time_taken = measure_sort_time(merge_sort, arr)
    print(f"Time taken to sort list of size {size}: {time_taken:.6f} seconds")
