import improvedMunkres
import ver2
import numpy as np

Max = 1
N = 100
k=4

s = np.random.rand(N, 2) * Max
e = np.random.rand(N, 2) * Max

print("ver1")
print(improvedMunkres.improved_munkres(s,e,Max,N,k))

print("ver2")
print(ver2.improved_munkres(s,e,Max,N,k))



