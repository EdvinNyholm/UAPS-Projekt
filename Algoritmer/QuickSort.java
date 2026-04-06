package Algoritmer;
public class QuickSort {

    public static void quickSort(int[] A, int start, int end) {

        if (start >= end) {
            return; // basfall
        }

        int pivotIndex = partition(A, start, end);

        quickSort(A, start, pivotIndex - 1); // vänster del
        quickSort(A, pivotIndex + 1, end);   // höger del
    }

    private static int partition(int[] A, int start, int end) {

        int pivot = A[end]; // välj sista elementet som pivot
        int i = start - 1;

        for (int j = start; j < end; j++) {

            if (A[j] <= pivot) {
                i++;
                swap(A, i, j);
            }
        }

        swap(A, i + 1, end);

        return i + 1;
    }

    private static void swap(int[] A, int i, int j) {

        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }

}