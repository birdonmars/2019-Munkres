import time
import munkres
import kmeansclustering
import matplotlib.pyplot as plt
import numpy as np
import math
import copy


def improved_munkres(s, e, Max, N, k):

    def print_list(s):
        for i in s:
            print(i)

    def plot_fig():
        # plot
        plt.Figure()
        plt.title('Random Locations')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.scatter(s[:, 0], s[:, 1], color='red', label='start')
        plt.scatter(e[:, 0], e[:, 1], c='black', label='destination')
        plt.legend()
        plt.xlim([0, Max])
        plt.ylim([0, Max])
        plt.show()

    def plot_k_result():
        colors = ['r', 'g', 'b', 'y', 'c', 'm']
        for i in range(k):
            points = np.array([e[j] for j in range(len(e)) if idx[j] == i])
            plt.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
        plt.scatter(C[:, 0], C[:, 1], marker='x', s=200, c='#050505')
        plt.show()

    def plot_s_result():
        colors = ['r', 'g', 'b', 'y', 'c', 'm']
        for i in range(k):
            points = np.array([e[j] for j in range(len(e)) if idx[j] == i])
            #plt.scatter(points[:, 0], points[:, 1], s=20, c=colors[i], marker='x', label='destination')
            points = np.array([s[j] for j in range(len(s)) if start_idx[j] == i])
            plt.scatter(points[:, 0], points[:, 1], s=12, c=colors[i], label='start')
            plt.scatter(C[:, 0], C[:, 1], marker='x', s=200, c='#050505',label='centroid')
        #plt.legend()
        plt.xlim([0, Max])
        plt.ylim([0, Max])
        plt.show()

    def dist(a, b):
        return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))

    def cal_costmat(a, b):
        for i in range(len(a)):
            costMat[i][0] = i
            for j in range(len(b)):
                costMat[i][j+1] = dist(b[j, :], a[i, :])

    def cnt_idx():
        for j in range(k):
            cnt = 0
            for i in range(N):
                if idx[i] == j:
                    cnt += 1
            idxcnt[j] = cnt

    def struct_sort():
        for i in range(k):
            sorted_arr = sorted(costMat, key=lambda costMat: costMat[i+1])
            #print_list(sorted_arr)
            j = 0
            count = 0
            while count < idxcnt[i]:
                #print(start_idx)
                if start_idx[sorted_arr[j][0]] == -1:
                    start_idx[sorted_arr[j][0]] = i
                    count += 1
                j += 1


    '''
    -------------------------------
    Improved Munkres Start
    -------------------------------
    '''

    # k mean clustering
    [C, idx] = kmeansclustering.k_means(e, k)

    #print(idx)
    #print('k mean clustering...')
    #plot_k_result()




    # Generate Cost Matrix
    costMat = [[0 for j in range(k+1)] for i in range(N)]
    cal_costmat(s, C)
    # print_list(costMat)

    # Count idx
    idxcnt = [0] * k
    cnt_idx()

    # Struct Sort
    start_idx = [-1]*N
    struct_sort()

    if __name__ == '__main__':
        plot_s_result()


    #print("idx: ", idx)
    #print("idxcnt: ", idxcnt)
    #print("Start idx: ",start_idx)


    # idx list _s, e 는 idx-->Centroid number list 내에 들어있는건 매칭된 점들
    idxlist_s = [[] for i in range(k)]

    for i in range(N):
        idxlist_s[start_idx[i]].append(i)

    #print_list(idxlist_s)

    idxlist_e = [[] for i in range(k)]
    for i in range(N):
        idxlist_e[idx[i]].append(i)

    #print_list(idxlist_e)


    # Munkres divided
    ans = 0
    m = munkres.Munkres()
    for i in range(k):
        costMat = [[0 for j in range(idxcnt[i]+1)] for k in range(idxcnt[i])]
        cal_costmat(np.array([s[j] for j in range(len(s)) if start_idx[j] == i]),
                    np.array([e[j] for j in range(len(e)) if idx[j] == i]))
        costMat = np.array(costMat)
        costMat = costMat[:, 1:]
        #print(costMat)
        cpy = copy.deepcopy(costMat)
        indexes = m.compute(costMat)
        total_cost = 0
        for r, c in indexes:
            x = cpy[r][c]
            total_cost += x
            #print('(%d, %d) -> %f' % (idxlist_s[i][r], idxlist_e[i][c], x))
        #print('lowest cost=%f' % total_cost)
        ans+=total_cost

    if __name__ == '__main__':
        print("Min cost: %f" %ans)

    return ans



def original_munkres(s, e, Max, N, k):

    def dist(a, b):
        return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))


    def cal_costmat(a, b):
        for i in range(len(a)):
            costMat[i][0] = i
            for j in range(len(b)):
                costMat[i][j+1] = dist(b[j, :], a[i, :])

    '''
    -------------------------------------
    original
    -------------------------------------
    '''
    ans = 0
    m = munkres.Munkres()
    costMat = [[0 for j in range(N+1)] for k in range(N)]
    cal_costmat(s, e)
    costMat = np.array(costMat)
    costMat = costMat[:, 1:]
    # print(costMat)
    cpy = copy.deepcopy(costMat)
    indexes = m.compute(costMat)
    total_cost = 0
    for r, c in indexes:
        x = cpy[r][c]
        total_cost += x
        #print('(%d, %d) -> %f' % (r, c, x))
    if __name__ == '__main__':
        print("Min cost: %f" %total_cost)

    return total_cost

    '''
    --------------------------------------
    End
    --------------------------------------
    '''


if __name__ == '__main__':

    Max = 1
    N = 50
    k = 4

    # Generate Random Matrix
    s = np.random.rand(N, 2) * Max
    e = np.random.rand(N, 2) * Max

    improved_munkres(s, e, Max, N, k)
    # original_munkres(s,e,Max,N,k)