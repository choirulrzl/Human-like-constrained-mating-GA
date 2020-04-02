import numpy as np

x = [2,3]

def hitung(x):
    a = np.sum([(x[i])for i in range(len(x))])
    print(a)

D = 5
a = [i+1 for i in range(len(x))]

print(a)