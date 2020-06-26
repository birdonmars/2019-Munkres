import improvedMunkres
import time
import numpy as np
import matplotlib.pylab as plt
import ver2
import pandas as pd

colors = ['r.-', 'g.-', 'b.-', 'y.-', 'c.-', 'm.-']



def change_N(Max, k, end,n_loop):

    i_time = [0] * (end-k)
    d_time = [0] * (end-k)
    g_time = [0] * (end - k)

    for N in range(k, end):
        for loop in range(n_loop):

            s = np.random.rand(N, 2) * Max
            e = np.random.rand(N, 2) * Max

            start_time = time.time()
            improvedMunkres.improved_munkres(s, e, Max, N, k)
            print("---%s seconds ---" % (time.time() - start_time))
            i_time[N-k] += time.time() - start_time

            start_time = time.time()
            ver2.improved_munkres(s, e, Max, N, k)
            print("---%s seconds ---" % (time.time() - start_time))
            g_time[N - k] += time.time() - start_time

            start_time = time.time()
            ver2.original_munkres(s, e, Max, N, k)
            print("---%s seconds ---" % (time.time() - start_time))
            d_time[N-k] += time.time() - start_time

            list(range(k, end))

        i_time[N-k] /= n_loop
        g_time[N-k] /= n_loop
        d_time[N-k] /= n_loop


    plt.title('Execution time difference')

    plt.plot(list(range(k, end)), d_time, 'kv-', label='mode 1')
    plt.plot(list(range(k, end)), i_time, 'r.-', label='mode 2')
    plt.plot(list(range(k, end)), g_time, 'b.-', label='mode 3')
    plt.xlabel('number of robots')
    plt.ylabel('time(s)')
    plt.legend()
    plt.show()


def change_N_2(Max, k, end,n_loop):

    i_time = [0] * (end-k)
    d_time = [0] * (end-k)
    g_time = [0] * (end - k)

    for NNN in range(k, end):
        N = NNN*50
        for loop in range(n_loop):

            s = np.random.rand(N, 2) * Max
            e = np.random.rand(N, 2) * Max

            start_time = time.time()
            improvedMunkres.improved_munkres(s, e, Max, N, k)
            print("---%s seconds ---" % (time.time() - start_time))
            i_time[NNN] += time.time() - start_time

            start_time = time.time()
            ver2.improved_munkres(s, e, Max, N, k)
            print("---%s seconds ---" % (time.time() - start_time))
            g_time[NNN] += time.time() - start_time

            # start_time = time.time()
            # ver2.original_munkres(s, e, Max, N, k)
            # print("---%s seconds ---" % (time.time() - start_time))
            # d_time[N-k] += time.time() - start_time

            list(range(k, end))

        i_time[NNN] /= n_loop
        g_time[NNN] /= n_loop
        # d_time[N-k] /= n_loop

    dataframe = pd.DataFrame(i_time)
    dataframe.to_csv("i_time.csv")
    dataframe = pd.DataFrame(g_time)
    dataframe.to_csv("g_time.csv")



    # plt.title('Execution time difference')
    #
    # # plt.plot(list(range(k, end)), d_time, 'kv-', label='mode 1')
    # plt.plot(list(range(k, end)), i_time, 'r.-', label='mode 2')
    # plt.plot(list(range(k, end)), g_time, 'b.-', label='mode 3')
    # plt.xlabel('number of robots')
    # plt.ylabel('time(s)')
    # plt.legend()
    # plt.show()


def change_k(Max, k_end, loop, N, color):
    i_time = [0] * (k_end-1)
    d_time = [0] * (k_end-1)

    for i in range(1, k_end):
        i_sum = 0
        d_sum = 0

        for j in range(loop):
            s = np.random.rand(N, 2) * Max
            e = np.random.rand(N, 2) * Max

            start_time = time.time()
            improvedMunkres.improved_munkres(s, e, Max, N, i)
            print("%d%%---%s seconds ---" % ((i+1)*(j+1)/((k_end-3)*loop)*100, time.time() - start_time))
            i_sum += time.time() - start_time

        '''
            start_time = time.time()
            improvedMunkres.original_munkres(s, e, Max, N, i)
            print("%d%%---%s seconds ---" % ((i-1)/(k_end-1)*100 + j/loop*10, time.time() - start_time))
            d_sum += time.time() - start_time
        '''
        i_time[i-1] = i_sum/loop
        # d_time[i-1] = d_sum/loop


    plt.title('Check time by changing K')
    a = np.array(i_time)
    plt.plot(list(range(1, k_end)), a[0:k_end], colors[color], label='improved '+str(N))
    # plt.plot(list(range(1, k_end)), d_time, 'r.-', label='default')
    plt.xlabel('k')
    plt.ylabel('time(s)')
    plt.legend()
    plt.show()

    print(np.array(i_time))

    return i_time


'''
--------------------------------
Main
--------------------------------
'''
change_N(1, 7, 50, 1)
# change_N_2(1, 7, 50, 10)
# change_k(1, 15, 10, 100, 0)
#t = change_k(3, 35, 10, 50, 1)
#t = change_k(1, 90, 10, 100, 1)
#t = change_k(10, 150, 10, 300, 1)
#t = change_k(3, 30, 10, 1000, 1)

#print(t)
#change_k(1, 15, 10, 20, 1)


#change k의 리턴은 k=1일때 소요되는 시간이 0번 인덱스, n 일정

'''
ax1 = plt.subplot(2, 1, 1)
plt.plot(list(range(loop)), ians, 'y.-', label='improved')
plt.plot(list(range(loop)), oans, 'r.-', label='default')
plt.title('Min Cost Flow')
plt.ylabel('Cost')
plt.legend()
print(ax1)

ax2 = plt.subplot(2, 1, 2)
plt.title('Time')
plt.plot(list(range(loop)), itime, 'y.-', label='improved')
# plt.plot(list(range(loop)), otime, 'r.-', label='default')
plt.xlabel('loop')
plt.ylabel('N')
plt.legend()
print(ax2)

plt.tight_layout()
plt.show()
'''