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

Gaps = []
i,j = 0,0
while True:
    pratt_number = (2 ** i) * (3 ** j)
    if pratt_number > n:
        break
    Gaps.append(pratt_number)
    if i < j:
        j += 1
    else:
        i += 1

B = sorted(A)
timeS = time.time()
A = Shell_S(A)
timeE = time.time()
print(A==B, timeE - timeS)