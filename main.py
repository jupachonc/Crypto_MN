"""
cc_number = input('Ingrese el número de la tarjeta: \n\n')
exp_date = input('Ingrese la fecha de vencimiento de l a tarjeta \n MMAA: \n\n')
cvv2 = input('Ingrese el código de seguridad CVV2 que se encuentra al respaldo de su tarjeta:\n\n')
"""
import numpy as np
from scipy.linalg import circulant
from methods import *
from utils import *



cc_number = "4000001234567899"
exp_date = "1220"
cvv2 = "123"
def find_system():

    zeros = False
    equal = False

    while not zeros or not equal:

        #Flags
        zeros = False
        equal = False

        #Generate Random Matrix and Permutation
        gmtx = np.random.randint(1000, size=(5,5))
        sigma = np.concatenate(([[1, 2, 3, 4, 5]], [np.random.permutation([1, 2, 3, 4, 5])]), axis=0)

        #Generate l Vector
        l = np.random.randint(1000, size=(5))
        l_c = circulant(get_permutation(l, sigma[1]))

        #Generate x Vector
        x = get_x(l_c)

        # Solve System Equations
        y = Gauss_Jordan(gmtx, x)
        y_2 = lu_method(gmtx, x)

        print(y)
        print(y_2)

        zeros = not (0 in y or 0 in y_2)
        equal = y == y_2

        if zeros and equal:
            return gmtx, x, sigma, l, l_c, y

def encrypt(cc_number, exp_date, cvv2):
    dict_array = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    txt_data = cc_number + " " + exp_date + " " + cvv2

    mtx_data = []

    i = 0

    for _ in range(5):
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

    gmtx, x, sigma, l, l_c, y = find_system()

    gmtx = np.random.randint(1000, size=(5,5))
    sigma = np.concatenate(([[1, 2, 3, 4, 5]], [np.random.permutation([1, 2, 3, 4, 5])]), axis=0)
    x = []

    l = np.random.randint(1000, size=(5))
    l_c = circulant(get_permutation(l, sigma[1]))

    x = get_x(l_c)

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


encrypt(cc_number, exp_date, cvv2)