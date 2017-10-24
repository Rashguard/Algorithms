def partition(A, p, r):
    x = A[r-1]
    i = p - 1
    for j in range(p,r-1):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r-1] = A[r-1],A[i+1]
    return i+1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)
