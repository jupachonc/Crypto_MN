"""
cc_number = input('Ingrese el número de la tarjeta: \n\n')
exp_date = input('Ingrese la fecha de vencimiento de l a tarjeta \n MMAA: \n\n')
cvv2 = input('Ingrese el código de seguridad CVV2 que se encuentra al respaldo de su tarjeta:\n\n')
"""
import numpy as np
from scipy.linalg import circulant
from methods import *

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




cc_number = "4000001234567899"
exp_date = "1220"
cvv2 = "123"

dict_array = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

txt_data = cc_number + " " + exp_date + " " + cvv2

mtx_data = []

i = 0

for x in range(5):
    line = []
    for y in range(5):
        c = txt_data[i]
        if c == " ":
            line.append(" ")
        else:
            line.append(dict_array[int(c)])
        i += 1
    mtx_data.append(line)

s = num_codec(mtx_data)

gmtx = np.random.randint(1000, size=(5,5))
sigma = np.concatenate(([[1, 2, 3, 4, 5]], [np.random.permutation([1, 2, 3, 4, 5])]), axis=0)
x = []

l = np.random.randint(1000, size=(5))
l_c = circulant(get_permutation(l, sigma[1]))

x = get_x(l_c)

y = Gauss_Jordan(np.concatenate((gmtx, x), axis = 1))

y_c = circulant(get_permutation(y, sigma[1]))

p = np.matmul(l_c, np.matmul(gmtx, y_c))


#Encryption

x_1 = circulant(np.random.randint(1000, size=(5)))
x_2 = circulant(np.random.randint(1000, size=(5)))


d_1 = np.matmul(x_1, np.matmul(gmtx, x_2))
matmtx = np.matmul(x_1, np.matmul(p, x_2))
d_2 = np.bitwise_xor(matmtx, s)

print(s)

auxs = np.matmul(np.matmul(l_c, d_1), y_c)
s_dec = np.bitwise_xor(auxs, d_2)

print(s_dec)