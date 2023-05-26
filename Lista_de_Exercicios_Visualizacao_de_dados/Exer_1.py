
'''
Problema 1

Este é um conjunto de dados clássico usado em muitos tutoriais e demos de mineração de dados 
- perfeito para iniciar a análise exploratória e construir modelos de classificação binários 
para prever a sobrevivência.

Os dados abrangem apenas os passageiros, não a tripulação.
As characteristic's dos dados são

    survived - Sobrevivente (0 = Não; 1 = Sim)
    pclass - Classe do passageiro
    sex - Sexo
    age - Idade
    sibsp - Número de irmãos/cônjuges a bordo
    parch - Número de pais/filhos a bordo
    fare - Tarifa do passageiro
    embark_town - Porto de embarque
    class - Classe do passageiro
    who - informa se era homem, mulher ou criança
    alone - informa se o passageiro estava sozinho




'''
import seaborn as sns
import pandas as pd

#importando dados

dados=sns.load_dataset('titanic') 
dados.head()
#criando um datafram a partir dos dados
#print(dados)
print(dados.head(4))
