class BubbleSort:

    @staticmethod
    def bubbleSort(A):

        for i in range(len(A) - 1):

            for j in range(len(A) - 1):

                if A[j] > A[j + 1]:

                    temp = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = temp