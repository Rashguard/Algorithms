x = [40694, 73593, 13612, 65541, 19386, 2347, 26723, 42533, 27999, 96272, 2222]

def insort(A):
    for j in range (1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

def bubblesort(A):
    for i in range (0, len(A)-1):
        for j in range (0, len(A)-(i+1)):
            if A[j] > A[j+1]:
                key = A[j+1]
                A[j+1] = A[j]
                A[j] = key

def fac(n):
    if n<=1:
        return 1
    else:
        return n*fac(n-1)

