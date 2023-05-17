'''


Essa lista contém questões práticas incluindo os seguintes tópicos com numpy.

    Criação de array e seus atributos, intervalos numéricos em numPy
    Slicing e indexação de NumPy Array.
    Manipulação, pesquisa, classificação e divisão de arrays.
    Funções matemáticas com arrays e broadcasting arrays NumPy.


'''

import numpy as np
import math


#definindo soma

def soma_array(matriz_1, matriz_2):
    matriz_1 = np.array(matriz_1)
    matriz_2 = np.array(matriz_2)
    resultado = matriz_1 + matriz_2
    return resultado.tolist()

            
#definindo a subtração


import numpy as np

def subtracao_array(matriz_1, matriz_2):
    matriz_1 = np.array(matriz_1)
    matriz_2 = np.array(matriz_2)
    resultado = matriz_1 - matriz_2
    return resultado.tolist()



#definindo a multiplicação 

import numpy as np

def mult_array(matriz_1, matriz_2):
    matriz_1 = np.array(matriz_1)
    matriz_2 = np.array(matriz_2)
    resultado = matriz_1 * matriz_2
    return resultado.tolist()


#definindo a divisão


import numpy as np

def divisao_array(matriz_1, matriz_2):
    matriz_1 = np.array(matriz_1)
    matriz_2 = np.array(matriz_2)
    resultado = matriz_1 / matriz_2
    return resultado.tolist()

#criando array
array_04 = np.array([1, 2, 3])
array_05 = np.array([[1, 2, 3], [4, 5, 6]])

resultado_soma=soma_array(array_04,array_05)

resultado_subtracao=subtracao_array(array_04,array_05)

resultado_multiplicacao=mult_array(array_04,array_05)


resultado_divisao=divisao_array(array_04,array_05)
print("soma:\n",resultado_soma)

print("subtração:\n",resultado_subtracao)

print("multiplicacao:\n",resultado_multiplicacao)

print("divisao:\n",resultado_divisao)
