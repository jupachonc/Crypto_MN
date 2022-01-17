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