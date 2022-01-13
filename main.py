"""
cc_number = input('Ingrese el número de la tarjeta: \n\n')
exp_date = input('Ingrese la fecha de vencimiento de l a tarjeta \n MMAA: \n\n')
cvv2 = input('Ingrese el código de seguridad CVV2 que se encuentra al respaldo de su tarjeta:\n\n')
"""

import numpy as np
from scipy.linalg import circulant


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

print(mtx_data)

g_mtx = [
        [10, 9, 18, 20, 2], 
        [9, 30, 44, 28,19], 
        [20, 18, 36, 40, 4], 
        [18, 60, 88, 56, 38], 
        [40, 36, 72, 80, 8]
        ]

l = [160, 320, 78, 80, 39]

l_c = [78, 320, 80, 160, 39]

lc_circulant = circulant(np.array(l_c))

sigma = [[1, 2, 3, 4, 5], [3, 5, 4, 1, 2]]

x = []

for k in range(5):
    x.append(lc_circulant[k][3])

print(lc_circulant)