import random
import time

def Bubble_S(A):
    for i in range(1,n):
        for j in range(1, n-i):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A


n = 10000
A = [0]*n
for i in range (1,n):
    A[i] = random.randint(1,n//2)

B = sorted(A)
timeS = time.time()
A = Bubble_S(A)
timeE = time.time()
print(A==B, timeE - timeS)