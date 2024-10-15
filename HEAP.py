import random
import time

def Heap_S(A):
    buildMaxHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0],A[i] = A[i],A[0]
        HeapMax(A, 0, i)

    return A

def buildMaxHeap(A):
    start = (len(A)-2)//2
    while start >=0:
        HeapMax(A,start, len(A))
        start -= 1

def HeapMax(A, index, size):
    l = 2*index+1
    r = 2*index+2

    if (l<size and A[l]>A[index]):
        largest = l
    else:
        largest = index

    if (r<size and A[r]>A[largest]):
        largest = r

    if (largest != index):
        A[largest], A[index] = A[index], A[largest]
        HeapMax(A,largest,size)


n = 10000
A = [0]*n
for i in range (1,n):
    A[i] = random.randint(1,n//2)

B = sorted(A)
timeS = time.time()
A = Heap_S(A)
timeE = time.time()

print(A==B, timeE - timeS)