import random
import time

def Quick_S(A):
    if len(A) > 1:
        pivot = random.choice(A)
        smaller = []
        bigger = []
        same = []
        for a in A:
            if a<pivot:
                smaller.append(a)
            elif a == pivot:
                same.append(a)
            else:
                bigger.append(a)
        return Quick_S(smaller)+same+Quick_S(bigger)
    else:
        return A


n = 10000
A = [0]*n
for i in range (1,n):
    A[i] = random.randint(1,n//2)

B = sorted(A)
timeS = time.time()
A = Quick_S(A)
timeE = time.time()
print(A==B, timeE - timeS)