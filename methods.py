import numpy as np

def Gauss_Jordan(A):
    """
    O algoritmo de Gauss-Jordan serve para resolver sistemas lineares de forma analítica.
    Não apresenta problemas de divergência, resolvendo todos casos com solução possível e única.
    O primeiro grande ciclo escalona a primeira metade. O primeiro ciclo interno divide pelos pivôs.
    O segundo ciclo é a multiplicação pelo elemento pivô, de modo a zerar
    O ciclo maior inicia pela primeira coluna e se repete até a penúltima coluna
    """
    n = len(A)
    #primeira metade do escalonamento
    for j in range(0,n): #correndo ao longo das colunas
        for i in range(j,n):
            A[i,:] = A[i,:]/A[i,i] #divisão pelos pivôs
        for i in range(j+1,n):
            A[i,:] = -A[j,:]*A[i,j] + A[i,:]
    
    #segunda metade do escalonamento    
    for j in range(1,n):
        for i in range(1,n):
            A[n-j-i,:] = A[n-j-i,:] - A[n-j,:]*A[n-j-i,n-j]
    
    y = A[:,n] #vetor com resultados
    return y




##############################################

#Método de Gauss-Seidel

# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

def seidel(a, x ,b):
	#Finding length of a(5)	
	n = len(a)				
	# for loop for 5 times as to calculate x, y , z
	for j in range(0, n):		
		# temp variable d to store b[j]
		d = b[j]				
		
		# to calculate respective xi, yi, zi
		for i in range(0, n):	
			if(j != i):
				d-=a[j][i] * x[i]
		# updating the value of our solution		
		x[j] = d / a[j][j]
	# returning our updated solution		
	return x	

		
n = 5
				
x = [0, 0, 0, 0, 0]						
a = np.random.randint(1000, size=(5, 5)) 
b = np.random.randint(10, size=(5)) 

sol = []

for i in range(0, 25):
  x = seidel(a, x, b)
  if i == 24:
    sol = x

print(sol)




################################################################

#Método de Jacobi

#! /usr/bin/python3.3
import numpy as np
from math import sqrt, copysign


def spherical_matrix_norm(matrix):
    """ Returns sum of square of elements in matrix: for diagonal, not diagonal and total """
    diag_sum = sum([matrix[i, i] ** 2 for i in range(len(matrix))])
    non_diag_sum = sum([matrix[i, j] ** 2 for i in range(len(matrix)) for j in range(len(matrix)) if not i == j])
    total_sum = sum([matrix[i, j] ** 2 for i in range(len(matrix)) for j in range(len(matrix))])
    return (diag_sum, non_diag_sum, total_sum)


def max_non_diag_elem(matrix):
    """ Returns indexes (i,j) of max non-diagonal element """
    matrix = np.array(matrix).tolist()
    max_element_value = max([max(x[:k] + x[k + 1:]) for k, x in enumerate(matrix)])
    indexes = [(subarray.index(max_element_value), i) for i, subarray in enumerate(matrix) if max_element_value in subarray and i != subarray.index(max_element_value)]
    return indexes[0]


def matrix_rotarion(matrix, max_i, max_j):
    """ Indexes of max non-diagonal element given, transforms matrix for annulment of this element"""
    res_matrix = np.identity(len(matrix))
    mu = 2 * matrix[max_i, max_j] / (matrix[max_i, max_i] - matrix[max_j, max_j])
    c = sqrt(0.5 * (1 + 1 / sqrt(1 + mu ** 2)))
    s = sqrt(0.5 * (1 - 1 / sqrt(1 + mu ** 2))) * copysign(1, mu)
    res_matrix[max_i, max_i] = c
    res_matrix[max_j, max_j] = c
    res_matrix[max_i, max_j] = s
    res_matrix[max_j, max_i] = -s
    return res_matrix


def transform_matrix(matrix, eps):
    """ Transformes matrix according to Jacobi method """
    while (matrix[max_non_diag_elem(matrix)[0],max_non_diag_elem(matrix)[1]] > eps):        
        elem_i, elem_j = max_non_diag_elem(matrix)
        rotation_step = matrix_rotarion(matrix, elem_i, elem_j)
        matrix = rotation_step.dot(matrix).dot(rotation_step.transpose())  
        # printed results for report
        # print('spherical matrix norm (diag_sum, non_diag_sum, total_sum)\n ',spherical_matrix_norm(matrix))
        # print('T(i,j) \n', rotation_step,'\n')
        # print('T(i,j)-transposed \n', rotation_step.transpose(),'\n')    
    return matrix


def find_eigenvalues(matrix):
    """ Returns eigenvalues - works for already tranformed matrix """
    return ([matrix[i,i] for i in range(len(matrix))])


print("NCM: Assignment #4: Finding eigenvalues - Jacobi eigenvalue algorithm \n")
eps = 0.00001
A = np.random.randint(1000, size=(5, 5)) 
print(' Start with matrix: \n', A, '\n Precision e = ', eps)	
tranformed = transform_matrix(A,eps)	
print ('\n Result: \n',find_eigenvalues(tranformed))