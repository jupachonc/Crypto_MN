from idna import decode
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

def encode_matrix(cc_number, exp_date, cvv2):
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

    return mtx_data

def num_decode(data):
    dictionary = {
        11 : "A",
        12 : "B",
        13 : "C",
        14 : "D",
        15 : "E",
        16 : "F",
        17 : "G",
        18 : "H",
        19 : "I",
        20 : "J", 
        21 : "K", 
        22 : "L", 
        23 : "M", 
        24 : "N", 
        25 : "O", 
        26 : "P", 
        27 : "Q", 
        28 : "R", 
        29 : "S", 
        30 : "T", 
        31 : "U", 
        32 : "V", 
        33 : "W", 
        34 : "X", 
        35 : "Y", 
        36 : "Z", 
        99 : " "
    
    }

    decode_mtx = []
    for i in range(5):
        line = []
        for j in range(5):
            line.append(dictionary[data[i][j]])
        decode_mtx.append(line)
    
    return decode_mtx

def decode_matrix(data):
    dictionary = {
        "J": 0,
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9
    }

    decode_mtx = []

    for i in range(5):
        line = []
        for j in range(5):
            c = data[i][j]
            if c == " ":
                line.append(" ")
            else:
                line.append(dictionary[c])
        decode_mtx.append(line)

    return decode_mtx

def print_decrypt(mtx):
    txt = ''
    for line in mtx:
        for c in line:
            txt += str(c)
    
    print("\n\nDecrypted Data\n")
    print(txt, end='\n\n')