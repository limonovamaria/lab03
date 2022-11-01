import numpy as np
n = int(input("n="))
a = np.zeros(n)
for i in range (0,n):
    a[i] = int(input())

for i in range(0,n):
    for j in range(i,n):
        if (a[j]<a[i]):
            b = a[i]
            a[i] = a[j]
            a[j] = b


for i in range (0,n):
    print(a[i])