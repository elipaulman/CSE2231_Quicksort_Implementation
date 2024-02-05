# Elijah Paulman - QuickSort Implementation

import random
import time
import unittest
import matplotlib.pyplot as plt
import math

# quicksort algorithm implementation
def quicksort(arr):
    # edge case
    if len(arr) <= 1:
        return arr
    # create pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# generate random array of size filled with random integers
def createRandomArray(size):
    return [random.randint(0, 1000) for _ in range(size)]

# computes time to execute and returns both the array size and the runtime
def computeRunTime(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return len(arr), end_time - start_time

# computes the expected runtime for quicksort, which is n log n
def expectedRunTime(n):
    return n * math.log(n)

# array sizes to test
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# lists to store the array sizes and runtimes
actual_runtimes = []
expected_runtimes = []

for size in sizes:
    arr = createRandomArray(size)
    arr_size, runtime = computeRunTime(quicksort, arr)
    actual_runtimes.append((arr_size, runtime))
    expected_runtimes.append((arr_size, expectedRunTime(arr_size)))

# plot the actual runtimes and expected runtimes
plt.plot(*zip(*actual_runtimes), label='Actual')
plt.plot(*zip(*expected_runtimes), label='Expected')
plt.xlabel('Array Size')
plt.ylabel('Runtime (seconds)')
plt.legend()
plt.show()

# unit test to make sure array is sorted
class TestQuickSort(unittest.TestCase):
    def testQuicksort(self):
        # Test with array of size 1,000
        arr1 = createRandomArray(1000)
        # Make completely separate copy of the array
        arr2 = arr1.copy()
        print("Unsorted array (first 10 elements):", arr1[:10])
        sorted_arr = sorted(arr1)
        print("Python sorted array (first 10 elements):", sorted_arr[:10])
        
        # Compute and print the time taken for quicksort
        quick_sorted_arr = quicksort(arr2)
        quicksort_time = computeRunTime(quicksort, arr2)
        print("Quicksort sorted array (first 10 elements):", quick_sorted_arr[:10])
        print("Array comparison results: ", quick_sorted_arr == sorted_arr)
        print("Time taken for quicksort: ", round(quicksort_time, 5), "seconds.")
        
        self.assertEqual(quick_sorted_arr, sorted_arr)

# Tests run when directly running the file
if __name__ == "__main__":
    unittest.main()