def parent(n):
    return (n-1)//2

def left(n):
    return 2*n+1

def right(n):
    return 2*n+2

def heapify(A,i,heapsize):
    l = left(i)
    r = right(i)
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        heapify(A,largest,heapsize)

def buildheap(A):
    for i in range(len(A)//2 + 1,0,-1):
        heapify(A,i-1,len(A))

def heapsort(A):
    buildheap(A)
    for i in range(len(A),1,-1):
        print(A)
        A[i-1],A[0] = A[0],A[i-1]
        print(A)
        print
        heapify(A,0,i - 1)
