def merge(tmp,A,p,q,r):
    for i in range(p,r):
        tmp[i] = A[i]
    i = p
    j = q
    while i < q and j < r:
        if tmp[i] < tmp[j]:
            A[p] = tmp[i]
            i = i + 1
        else:
            A[p] = tmp[j]
            j = j + 1
        p = p + 1
    while i < q:
        A[p] = tmp[i]
        i = i + 1
        p = p + 1
    while j < r:
        A[p] = tmp[j]
        j = j + 1
        p = p + 1

def mergesort(tmp, A,p,r):
    if p < r - 1:
        q = (p + r) // 2
        mergesort(tmp, A,p,q)
        mergesort(tmp, A,q,r)
        merge(tmp, A,p,q,r)

def main():
    A = [2, 4, 6, 8, 1, 3]
    tmp = A[:]
    q = 4
    A = [6, 9, 5, 1, 3, 5, 4, 0, 7, 4]
    tmp = A[:]
    mergesort(tmp, A, 0, len(A))
    print(A)

main()
