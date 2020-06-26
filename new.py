import improvedMunkres
import time
import numpy as np
import matplotlib.pylab as plt

time_diff = 0

Max = 1
N = 100

for loop in range(100):

    s = np.random.rand(N, 2) * Max
    e = np.random.rand(N, 2) * Max

    # div 3
    st1 = time.time()
    improvedMunkres.improved_munkres(s, e, Max, N, 3)
    et1 = time.time() - st1

    st2 = time.time()
    improvedMunkres.original_munkres(s, e, Max, N, 3)
    et2 = time.time() - st2

    print("%f %f" % (et1, et2))

    '''
    print("trial : %d" % loop)
    print(et1/et2*100)
    time_diff += et1/et2*100
    '''


'''
print("Final::", end=' ')
print(time_diff/100)
'''



