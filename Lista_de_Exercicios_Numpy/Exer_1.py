'''


Essa lista contém questões práticas incluindo os seguintes tópicos com numpy.

    Criação de array e seus atributos, intervalos numéricos em numPy
    Slicing e indexação de NumPy Array.
    Manipulação, pesquisa, classificação e divisão de arrays.
    Funções matemáticas com arrays e broadcasting arrays NumPy.


'''

import numpy as np

'''
exercicio 1

Crie um array inteiro 4x2 e mostre seus atributos

Os elementos deven ser um tipo de int16 sem sinal. E imprima os seguintes atributos:
 formato do array; dimensões; comprimento de cada elemento do array.


'''


#nesse passo criamos um arranjo ou array matricial p
#obs:é importante deixar as colunas do array estruturado para deifinir o formato
criando_array=np.array([
            [1,4],
            [0,2],
            [1,3],
            [2,3]    
                ])
print("Aqui podemos verificar o formato do array:",criando_array.shape)
print("O aaray:\n",criando_array)
print("O tipo do array é:",criando_array.dtype)
#alterando o tipo de dado
criando_array=criando_array.astype(np.int16)
print("alterando o tipo de dado para um arra de inteiro sem sinal", criando_array.dtype)
print("Imprimindo o comprimento do array:",criando_array.size)

#imprimindo atributos

#-dimensão

print("Imprimindo a dimensão do array:",criando_array.ndim)