import numpy as np
import sys

# LU ===========================================================

MAX = 100
 
 
def luDecomposition(mat, n):
 
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]
 
    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):
 
        # Upper Triangular
        for k in range(i, n):
 
            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
 
            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum
 
        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:
 
                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
 
                # Evaluating L(k, i)
                lower[k][i] = float((mat[k][i] - sum) /
                                  upper[i][i])
 
    # setw is for displaying nicely
    print("Lower Triangular\t\t\t\tUpper Triangular")
 
    # Displaying the result :
    for i in range(n):
 
        # Lower
        for j in range(n):
            print("{:0.2f}".format(lower[i][j]), end="\t")
        print("", end="\t")
 
        # Upper
        for j in range(n):
            print("{:0.2f}".format(upper[i][j]), end="\t")
        print("")
    return lower, upper
 
def lu_method(gmtx, x):
    n = len(x)
    lower, upper = luDecomposition(gmtx, n)

    l_sol = [1] * n
    for i in range(n):
        sum = 0
        line = lower[i]
        for j in range(i+1):
            if i != j:
                sum += line[j]*l_sol[j]
        l_sol[i] = (float(x[i])- sum)/line[i]

    u_sol = [1] * n
    for i in range(n-1, -1, -1):
        sum = 0
        line = upper[i]
        for j in range(n-1, -1, -1):
            if i != j:
                sum += line[j]*u_sol[j]
        u_sol[i] = (float(l_sol[i])-sum)/line[i]    

    print("\nSolución L\n")
    print([round(x, 2) for x in l_sol])
    print("\n\nSolución U\n")
    print([round(x, 2) for x in u_sol], end="\n\n")
    

    return [round(x) for x in u_sol]


def Gauss_Jordan(gmtx, x_):
    # Reading number of unknowns
    n =  len(x_)

    # Making numpy array of n x n+1 size and initializing 
    # to zero for storing augmented matrix
    a = np.zeros((n,n+1))

    # Making numpy array of n size and initializing 
    # to zero for storing solution vector
    x = np.zeros(n)

    # Reading augmented matrix coefficients
    a = np.concatenate((gmtx, x_), axis = 1)

    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            print('Divide by zero detected!')
            return [0] * n
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    return [round(x_i) for x_i in x]