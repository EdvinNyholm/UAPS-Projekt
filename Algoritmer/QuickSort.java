package Algoritmer;

import java.util.ArrayList;
import java.util.Collections;

public class QuickSort {

    public static void quickSort(ArrayList<Integer> A, int left, int right) {
        if (left >= right) {
            return; // basfall
        }

        int pivotIndex = partition(A, left, right);

        
        quickSort(A, left, pivotIndex - 1); 
        quickSort(A, pivotIndex + 1, right);   
    }

    private static int partition(ArrayList<Integer> A, int left, int right) {
        // Vi väljer sista elementet som pivot
        int pivot = A.get(right); 
        int i = left - 1;

        for (int j = left; j < right; j++) {
            // Jämför objektens värden
            if (A.get(j) <= pivot) {
                i++;
                swap(A, i, j);
            }
        }

        // Placera pivot på rätt plats
        swap(A, i + 1, right);

        return i + 1;
    }

    private static void swap(ArrayList<Integer> A, int i, int j) {
        // I ArrayList måste vi använda set() och get() istället för [index]
        int temp = A.get(i);
        A.set(i, A.get(j));
        A.set(j, temp);
    }
}