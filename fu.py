import improvedMunkres
import time
import numpy as np
import matplotlib.pylab as plt
import ver2
import pandas as pd

colors = ['r.-', 'g.-', 'b.-', 'y.-', 'c.-', 'm.-']

def change_N(Max, k, end,n_loop):

    data = [[], [], []]

    for N in range(100, end, 100):

        mode2 = 0
        mode3 = 0

        for loop in range(n_loop):

            s = np.random.rand(N, 2) * Max
            e = np.random.rand(N, 2) * Max

            start_time = time.time()
            improvedMunkres.improved_munkres(s, e, Max, N, k)
            print("%d---%s seconds ---" % (N,time.time() - start_time))
            mode2 += time.time() - start_time

            start_time = time.time()
            ver2.improved_munkres(s, e, Max, N, k)
            print("%d---%s seconds ---" % (N,time.time() - start_time))
            mode3 += time.time() - start_time

        data[0].append(N)
        data[1].append(mode2 / n_loop)
        data[2].append(mode3/n_loop)

    dataframe = pd.DataFrame(data)
    dataframe.to_csv("data.csv")

def change_cluster(Max,N, start, end ,jump ,n_loop):

    data = [[],[]]

    for k in range(start, end, jump):

        result = 0

        s = np.random.rand(N, 2) * Max
        e = np.random.rand(N, 2) * Max

        s_time = time.time()
        result = ver2.improved_munkres(s, e, Max, N, k)
        time_result = time.time()-s_time

        data[0].append(k)
        data[1].append(result)

        print(k)

    dataframe = pd.DataFrame(data)
    dataframe.to_csv("err_data.csv")


change_N(1, 100, 1100, 1)
# change_cluster(1,1000,10,20,10,1)