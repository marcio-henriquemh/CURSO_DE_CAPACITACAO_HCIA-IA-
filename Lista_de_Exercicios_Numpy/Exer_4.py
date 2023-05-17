'''


Essa lista contém questões práticas incluindo os seguintes tópicos com numpy.

    Criação de array e seus atributos, intervalos numéricos em numPy
    Slicing e indexação de NumPy Array.
    Manipulação, pesquisa, classificação e divisão de arrays.
    Funções matemáticas com arrays e broadcasting arrays NumPy.


'''

import numpy as np

'''
exercicio 4

Retorne um array com os valores 
presentes nas linhas ímpares com colunas pares baseado no seguinte array

'''


def retorno_de_valores_impares(matriz):
    valores_da_matriz=[]

    for i in range(len(matriz)):
        if i% 2!=0:# verificar se a inha é impar
            for j in range(len(matriz[i])):
                if j % 2 ==0: #verificar se a coluna é par
                     valores_da_matriz.append(matriz[i][j])


    
    return valores_da_matriz

criando_array = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

resultado=retorno_de_valores_impares(criando_array)

print(resultado)
