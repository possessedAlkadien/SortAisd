import random
import time

def Selection_S(A):
    for i in range(1,n):
        minimum = i
        for j in range(i+1, n):
            if A[j]<A[minimum]:
                minimum = j
        if minimum!=i:
            A[i],A[minimum] = A[minimum], A[i]
    return A


n = 10000
A = [0]*n
for i in range (1,n):
    A[i] = random.randint(1,n//2)

B = sorted(A)
timeS = time.time()
A = Selection_S(A)
timeE = time.time()
print(A==B, timeE - timeS)