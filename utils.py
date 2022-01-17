import numpy as np

def get_permutation(array, permutation):
    aux_array = []
    for i in range(len(array)):
        aux_array.append(array[permutation[i] - 1])
    return np.array(aux_array)

def get_x(lc):
    x = []
    for k in range(5):
        x.append([lc[k][3]])
    return np.array(x)

def num_codec(mtx):
    out_mtx = []
    codec = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25, 'P': 26, 'Q': 27, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35, 'Z': 36, ' ': 99}
    for l in mtx:
        out_l = []
        for c in l:
            out_l.append(codec[c])
        out_mtx.append(out_l)
    return np.array(out_mtx)
