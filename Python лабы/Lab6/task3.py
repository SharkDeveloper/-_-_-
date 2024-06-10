from multiprocessing import Pool, Manager, Array
import numpy as np
from random import randint
import multiprocessing


N=5

def generate_data():
    p = list()
    q = list()

    for i in range(N):
        p.append(randint(0,10000000))
        q.append(randint(0,10000000))
    return p,q

def calculate_cell(i, j):
    print("args",i, j, p, q, result)

    #result.acquire()
    result[i][j] = np.sqrt((q[j] - p[i]) ** 2)
    #result.release()


def build_matrix(p, q):

    i = [i for i in range(N)]
    j = [i for i in range(N) for j in range(N)]
    print("j: ",j)
    with Manager() as manager:
        result = manager.Array('i',np.zeros(N * N, dtype=int))
        with Pool(4) as pool:
            args = (i, j, p, q, result)
            r = pool.map(calculate_cell,i, j ,chunksize = 1)
            print("r: ", r)
            return result


if __name__ == '__main__':
    p, q = generate_data()
    R = build_matrix(p, q)
    print("R",R)