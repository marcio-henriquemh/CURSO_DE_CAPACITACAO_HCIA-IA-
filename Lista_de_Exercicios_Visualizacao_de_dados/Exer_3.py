'''
Problema 3

Verifique os tipos dos atributos e apresente a descrição dos atributos numéricos.

'''

import pandas as pd
import seaborn as sns
import statistics

#importando dados

dados=sns.load_dataset('titanic') 
print("Print dos dados \n")
dados_titanic=dados[['survived','pclass','age','sibsp','parch','fare']]
print(dados_titanic.describe())
tipo_atributo=dados_titanic.dtypes
print(tipo_atributo)


