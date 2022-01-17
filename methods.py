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