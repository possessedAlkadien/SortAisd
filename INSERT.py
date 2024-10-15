import random
import time

def Insert_S(A):
    for i in range(1,n):
        cur = i
        while (cur >=0 and A[cur-1]>A[cur]):
            A[cur-1],A[cur]=A[cur],A[cur-1]
            cur-=1

    return A


n = 10000
A = [0]*n
for i in range (1,n):
    A[i] = random.randint(1,n//2)

B = sorted(A)
timeS = time.time()
A = Insert_S(A)
timeE = time.time()
print(A==B, timeE - timeS)