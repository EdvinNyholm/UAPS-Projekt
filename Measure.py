import time
import numpy as np
import os
import subprocess
import csv

from Algoritmer.QuickSort import QuickSort
from Algoritmer.MergeSort import mergesort
from Algoritmer.MatrixMath import MatrixMath

# --- DATAHANTERING ---

def load_data(filename):
    filepath = os.path.join("Data", filename)
    with open(filepath, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]

def load_matrix(filename):
    filepath = os.path.join("Data", filename)
    matrix = []
    with open(filepath, "r") as f:
        for line in f:
            if line.strip():
                matrix.append([int(x) for x in line.split(",")])
    return matrix

def save_to_csv(name, all_batches):
    if not os.path.exists("Results"):
        os.makedirs("Results")
    filename = f"Results/{name}_full.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Batch", "Iteration", "Time_ns"])
        for batch_idx, times in enumerate(all_batches):
            for iter_idx, t in enumerate(times):
                writer.writerow([batch_idx + 1, iter_idx + 1, t])
    print(f"✅ Klart! Data sparad i: {filename}")

# --- MÄTMETODER ---

def run_python_batch(algo, filename, iterations):
    times = []
    if algo == "matrix":
        size = filename.replace("data", "").replace(".txt", "")
        A = load_matrix(f"matrix_a_{size}.txt")
        B = load_matrix(f"matrix_b_{size}.txt")
        for _ in range(iterations):
            start = time.perf_counter_ns()
            MatrixMath(A, B)
            times.append(time.perf_counter_ns() - start)
    else:
        data = load_data(filename)
        for _ in range(iterations):
            arr = data.copy()
            start = time.perf_counter_ns()
            if algo == "quick": QuickSort.quickSort(arr, 0, len(arr)-1)
            else: mergesort(arr)
            times.append(time.perf_counter_ns() - start)
    return times

def run_numpy_batch(algo, filename, iterations):
    times = []
    if algo == "matrix":
        size = filename.replace("data", "").replace(".txt", "")
        A = np.genfromtxt(os.path.join("Data", f"matrix_a_{size}.txt"), delimiter=',')
        B = np.genfromtxt(os.path.join("Data", f"matrix_b_{size}.txt"), delimiter=',')
        for _ in range(iterations):
            start = time.perf_counter_ns()
            np.matmul(A, B)
            times.append(time.perf_counter_ns() - start)
    else:
        data = np.array(load_data(filename))
        for _ in range(iterations):
            arr = np.copy(data)
            start = time.perf_counter_ns()
            if algo == "quick": np.sort(arr, kind='quicksort')
            else: np.sort(arr, kind='mergesort')
            times.append(time.perf_counter_ns() - start)
    return times

def run_java_batch(algo, filename, iterations):
    cmd = ["java", "MeasureJava", algo, filename, str(iterations)]
    if algo == "matrix":
        size = filename.replace("data", "").replace(".txt", "")
        cmd[2] = f"matrix_a_{size}.txt" # Byter ut 'dataX.txt' mot matrisfilen
        cmd.append(f"matrix_b_{size}.txt")

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Java-fel: {result.stderr}")
        return []
    return [int(line) for line in result.stdout.strip().splitlines()]


def main():
    # Inställningar för testet
    mode = "python"      # "python", "numpy", "java"
    algo = "quick"     # "quick", "merge", "matrix"
    data_size = "800"  # "50", "800", "5000"
    
    batches = 100      # Antalet yttre körningar
    iterations = 500   # Antaler innre körningar

    filename = f"data{data_size}.txt"
    all_results = []

    print(f"--- STARTAR BENCHMARK: {mode.upper()} {algo.upper()} ({data_size} element) ---")
    
    for b in range(batches):
        if (b + 1) % 10 == 0:
            print(f"Bearbetar batch {b + 1}/{batches}...")
            
        if mode == "python":
            batch_times = run_python_batch(algo, filename, iterations)
        elif mode == "numpy":
            batch_times = run_numpy_batch(algo, filename, iterations)
        elif mode == "java":
            batch_times = run_java_batch(algo, filename, iterations)
            
        if batch_times:
            all_results.append(batch_times)

    csv_name = f"{mode.capitalize()}_{algo.capitalize()}_{data_size}"
    save_to_csv(csv_name, all_results)

if __name__ == "__main__":
    main()