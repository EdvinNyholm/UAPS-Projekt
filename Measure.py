import time
import numpy as np
from QuickSort import QuickSort
from BubbleSort import BubbleSort

def load_data(filename):
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]

def run_python_quicksort(data):

    arr = data.copy()

    start = time.perf_counter_ns()

    QuickSort.quickSort(arr, 0, len(arr)-1)

    end = time.perf_counter_ns()

    return end - start


def run_python_bubblesort(data):

    arr = data.copy()

    start = time.perf_counter_ns()

    BubbleSort.bubbleSort(arr)

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

        elif algorithm == "bubble":
            t = run_python_bubblesort(data)

        elif algorithm == "numpy_merge":
            t = run_numpy_mergesort(data)

        print(f"Run {i}: {t} ns")


if __name__ == "__main__":
    main()