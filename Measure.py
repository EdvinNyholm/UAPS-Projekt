import time
import numpy as np
import os
from Algoritmer.QuickSort import QuickSort

def load_data(filename):
    filepath = os.path.join("Data", filename)
    
    with open(filepath, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]

def run_python_quicksort(data):

    arr = data.copy()

    start = time.perf_counter_ns()

    QuickSort.quickSort(arr, 0, len(arr)-1)

    end = time.perf_counter_ns()

    return end - start




def run_numpy_mergesort(data):

    arr = np.array(data)

    start = time.perf_counter_ns()

    np.sort(arr, kind="mergesort")

    end = time.perf_counter_ns()

    return end - start


def main():

    filename = "data50.txt"      # BYT DATAFIL HÄR
    algorithm = "numpy_merge"    # BYT ALGORITM HÄR
    runs = 5

    data = load_data(filename)

    for i in range(runs):

        if algorithm == "quick":
            t = run_python_quicksort(data)

        elif algorithm == "numpy_merge":
            t = run_numpy_mergesort(data)

        print(f"Run {i}: {t} ns")


if __name__ == "__main__":
    main()