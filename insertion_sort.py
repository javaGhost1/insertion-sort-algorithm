
A = [4,3,1,7,5,2,6]
def insertion_sort(A):
    """Arrange list in non-descending order"""

    for k in range(1, len(A)):
        cur = A[k]
        j = k

        while j>0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
            A[j] = cur

    print(A)

insertion_sort(A)