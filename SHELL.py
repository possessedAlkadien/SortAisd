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


n = 10000
A = [0]*n
for i in range (1,n):
    A[i] = random.randint(1,n//2)

Gaps = [0]*(n//10)
for i in range (1,n//10):
    Gaps[i] = random.randint(1,n//10//2)

B = sorted(A)
timeS = time.time()
A = Shell_S(A)
timeE = time.time()
print(A)
print(B)
print(A==B, timeE - timeS)