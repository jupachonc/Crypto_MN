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

        print("================== Soluciones ==================================================\n\n")
        print("LU Method ======================================================================\n")
        print(y_2)
        print("\nGauss Method ======================================================================\n")
        print(y)

        zeros = not (0 in y or 0 in y_2)
        equal = y == y_2

        if zeros and equal:
            return gmtx, x, sigma, l, l_c, y


def generate_keys():

    #Find Systemn of Equations
    gmtx, x, sigma, l, l_c, y = find_system()

    y_c = circulant(get_permutation(y, sigma[1]))
    p = np.matmul(l_c, np.matmul(gmtx, y_c))

    keys = {
        "Private_Key":{
            "l_c": l_c,
            "y_c": y_c
        },

        "Public_Key":{
            "G": gmtx,
            "P": p
        }
    }

    return keys


def encrypt(data, publicKey):

    #Read Public Key
    gmtx = publicKey["G"]
    p = publicKey["P"]

    #Encode Matrix Data
    s = num_codec(data)

    #Encryption =============================================

    #Generate Two Random Circulant Matrix 
    x_1 = circulant(np.random.randint(1000, size=(5)))
    x_2 = circulant(np.random.randint(1000, size=(5)))

    #Encrypt
    d_1 = np.matmul(x_1, np.matmul(gmtx, x_2))
    matmtx = np.matmul(x_1, np.matmul(p, x_2))
    d_2 = np.bitwise_xor(matmtx, s)

    return {
        "D1" : d_1,
        "D2" : d_2
    }


def decrypt(encrypted_data, privateKey):

    #Read Encrypted Data
    d_1 = encrypted_data["D1"]
    d_2 = encrypted_data["D2"]

    #Read Private Key
    l_c = privateKey["l_c"]
    y_c = privateKey["y_c"]
    
    print("\n\nDecrypting Data Using Private key\n\n")
    print(privateKey)

    #Decrypt
    auxs = np.matmul(np.matmul(l_c, d_1), y_c)
    s_dec = np.bitwise_xor(auxs, d_2)

    return s_dec


#encrypt(cc_number, exp_date, cvv2)

#print(generate_keys())