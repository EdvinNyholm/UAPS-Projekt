class QuickSort:

    @staticmethod
    def quickSort(A, start, end):

        if start >= end:
            return  # basfall

        pivotIndex = QuickSort.partition(A, start, end)

        QuickSort.quickSort(A, start, pivotIndex - 1)  # vänster del
        QuickSort.quickSort(A, pivotIndex + 1, end)    # höger del

    @staticmethod
    def partition(A, start, end):

        pivot = A[end]  # välj sista elementet som pivot
        i = start - 1

        for j in range(start, end):

            if A[j] <= pivot:
                i += 1
                QuickSort.swap(A, i, j)

        QuickSort.swap(A, i + 1, end)

        return i + 1

    @staticmethod
    def swap(A, i, j):

        temp = A[i]
        A[i] = A[j]
        A[j] = temp