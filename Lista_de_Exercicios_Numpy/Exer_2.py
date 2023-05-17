'''


Essa lista contém questões práticas incluindo os seguintes tópicos com numpy.

    Criação de array e seus atributos, intervalos numéricos em numPy
    Slicing e indexação de NumPy Array.
    Manipulação, pesquisa, classificação e divisão de arrays.
    Funções matemáticas com arrays e broadcasting arrays NumPy.


'''

import numpy as np

'''
exercicio 2

CCrie uma array de inteiros 5X2 com um intervalo 
entre 100 e 200, de modo que a diferença entre cada elemento seja 10


'''

#nesse passo criamos um arranjo ou array matricial p
#obs:é importante deixar as colunas do array estruturado para deifinir o formato
criando_array=(np.arange(100,200,10).reshape(5,2))
print(criando_array)
print("O formato do array é:",criando_array.shape)