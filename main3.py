from __future__ import division
from matplotlib import colors as mcolors
import improvedMunkres
import time
import numpy as np
import matplotlib.pylab as plt
import ver2

#colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
#print(list(colors.values()))


division = 5
Max = 1
d_limit = 20
N = 50
loop = 100

buf1 = []
buf2 = []
for i in range(division, d_limit):
    buf1.append(0)
    buf2.append(0)

for l in range(loop):

    s = np.random.rand(N, 2) * Max
    e = np.random.rand(N, 2) * Max

    s1 = time.time()
    standard = improvedMunkres.original_munkres(s,e,Max,N,1)
    print("%d #%dth standard: %f seconds"%(N, l,time.time()-s1))

    for k in range(division, d_limit):
        s1 = time.time()
        r1 = improvedMunkres.improved_munkres(s,e,Max,N,k)
        temp = (r1 - standard)/standard*100
        buf1[k-division] += temp

        s1 = time.time()
        r1 = ver2.improved_munkres(s,e,Max,N,k)
        temp = (r1 - standard)/standard*100
        buf2[k-division] += temp
        #print("----------- %f seconds s:%f i:%f %f" % (time.time() - s1, standard, r1, temp))


    err1 = []
    err2 = []

    for i in range(len(range(division, d_limit))):
        err1.append(100-buf1[i]/loop)
        err2.append(100-buf2[i]/loop)

print(err1)
print(err2)

plt.title("Accuracy")

standard = [100]*(d_limit-division)

# plt.plot(range(division, d_limit), standard, c="k", label='mode 1', marker='v')
plt.plot(range(division, d_limit), err1, c="r", label='mode 2', marker='.')
plt.plot(range(division, d_limit), err2, c="b", label='mode 3', marker='.')
plt.legend()
plt.xlabel("number of groups")
plt.ylabel("accuracy(%)")
plt.show()
