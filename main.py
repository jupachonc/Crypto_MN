from crypt import *
from utils import *

option = -1

keys = {}

data = {}

while option != 4:
    option = -1
    print("Elija una opción:\n\n1. Generate keys\n2. Encrypt\n3. Decrypt\n4. Quit\n\nOption >>> ", end='')
    try:
        option = int(input())
    except:
        print("\n\nWrong Option, choose one\n\n")
        pass

    if option == 1:
        keys = generate_keys()

        print("\n\n")
        print(keys)
        print("\n\n")

    elif option == 2:
        cc_number = input('Ingrese el número de la tarjeta: \n\n')
        exp_date = input('Ingrese la fecha de vencimiento de la tarjeta \nMMAA: \n\n')
        cvv2 = input('Ingrese el código de seguridad CVV2 que se encuentra al respaldo de su tarjeta:\n\n')
        dt = encode_matrix(cc_number, exp_date, cvv2)
        data = encrypt(dt, keys["Public_Key"])

        print("\n\nEncripted Data: \n\n")
        print(data)
        print("\n")
    
    elif option == 3:
        try:
            d = decrypt(data, keys['Private_Key'])
            decode_mtx = decode_matrix(num_decode(d))
            print_decrypt(decode_mtx)
        except:
            print("\n\nKeys error, is not possible decrypt \n\n")
    elif option == 4:
        break
    else:
        print("\n\nWrong Option, choose one\n\n")
