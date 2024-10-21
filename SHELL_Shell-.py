import random
import time

def Shell_S(A):
    dev = int(0.9*n)
    for gap in Gaps:
        for i in range (gap, dev):
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
    A[i] = n-i

Gaps = [0]
p = n//2
for i in range (1,n//2):
    p = p//2
    Gaps.append(p)
    if p==0:
        break

B = sorted(A)
timeS = time.time()
A = Shell_S(A)
timeE = time.time()
print(A==B, timeE - timeS)