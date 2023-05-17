'''


Essa lista contém questões práticas incluindo os seguintes tópicos com numpy.

    Criação de array e seus atributos, intervalos numéricos em numPy
    Slicing e indexação de NumPy Array.
    Manipulação, pesquisa, classificação e divisão de arrays.
    Funções matemáticas com arrays e broadcasting arrays NumPy.


'''

import numpy as np
import math
'''
exercicio 5

Crie um array de resultado somando os seguintes arrays.
 Em seguida, modifique o array resultante calculando o quadrado de cada elemento
'''
#definindo soma
def soma_array(matriz_1,matriz_2):

    resultado_array=[]

    for i in range(len(matriz_1)):
            linha=[]
            for j in range(len(matriz_2[i])):
                soma=matriz_1[i][j]+matriz_2[i][j]
                linha.append(soma)
            resultado_array.append(linha)
    return resultado_array
            


#funcao ao quadrado

def quadrado_array(matriz_1,matriz_2):

    resultado_array_quadrado=[]

    for i in range(len(matriz_1)):
            quadrado=[]

            for j in range(len(matriz_2[i])):
                soma=matriz_1[i][j]+matriz_2[i][j]**2
                resultado_array_quadrado.append(soma)

            resultado_array_quadrado.append(resultado_array_quadrado)
    return resultado_array_quadrado
            


#criando array 

criando_array_01 = np.array([[5, 6, 9], [21 ,18, 27]])
criando_array_02 = np.array([[15 ,33, 24], [4 ,7, 1]])
resultado=soma_array(criando_array_01,criando_array_02)
resultado_quadrado=quadrado_array(criando_array_01,criando_array_02)
print(resultado)
print("o resultado elevado ao quadrado",resultado_quadrado)
