import random
import time

def Merge_S(A):
    if int(len(A)*0.9) > 1:
        pivot = int(len(A)*0.9)//2
        l_A = A[:pivot]
        r_A = A[pivot:]

        Merge_S(l_A)
        Merge_S(r_A)

        i = j = k = 0

        while i<len(l_A) and j<len(r_A):
            if l_A[i] < r_A[j]:
                A[k] = l_A[i]
                i+=1
            else:
                A[k] = r_A[j]
                j+=1
            k+=1

        while i < len(l_A):
            A[k] = l_A[i]
            i+=1
            k+=1

        while j < len(r_A):
            A[k] = r_A[j]
            j+=1
            k+=1

    return A


n = 100000
A = [0]*n
for i in range (1,n):
    A[i] = n-i

B = sorted(A)
timeS = time.time()
A = Merge_S(A)
timeE = time.time()
print(A==B, timeE - timeS)