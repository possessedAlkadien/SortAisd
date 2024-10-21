import random
import time

def Shell_S(A):
    for gap in Gaps:
        for i in range (gap, n):
            j = i
            cur = A[i]
            while j>= gap and A[j-gap]>cur:
                A[j] = A[j-gap]
                j -= gap
            A[j] = cur
    return A


n = 100000
A = [0]*n
for i in range (1,n):
    A[i] = n-i

Gaps = [0]*(n//2)
for i in range (1,n//2):
    Gaps[i] = 2**i-1

B = sorted(A)
timeS = time.time()
A = Shell_S(A)
timeE = time.time()
print(A==B, timeE - timeS)