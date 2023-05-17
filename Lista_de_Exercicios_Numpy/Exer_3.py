'''


Essa lista contém questões práticas incluindo os seguintes tópicos com numpy.

    Criação de array e seus atributos, intervalos numéricos em numPy
    Slicing e indexação de NumPy Array.
    Manipulação, pesquisa, classificação e divisão de arrays.
    Funções matemáticas com arrays e broadcasting arrays NumPy.


'''

import numpy as np

'''
exercicio 3

Baseado no array fornecido. 
Retorne um array de itens com a terceira coluna de todas as linhas

'''


#definindo um funcao

def obter_3_matriz(matriz):
    terceira_coluna=[linha[2] for linha in matriz]
    return terceira_coluna
#nesse passo criamos um arranjo ou array matricial p
#obs:é importante deixar as colunas do array estruturado para deifinir o formato
criando_array=np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
retorno_array=obter_3_matriz(criando_array)

print(retorno_array)
