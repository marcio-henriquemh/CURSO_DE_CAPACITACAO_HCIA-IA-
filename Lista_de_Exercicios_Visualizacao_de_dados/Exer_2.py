'''



    Problema 2

    Calcule o total de sobreviventes, 
    idade média dos passageiros, e o número de homens e mulheres a bordo

'''


import pandas as pd
import seaborn as sns
import statistics


dados = sns.load_dataset('titanic')

def total_sobrevivente():
    total = 0
    sobrevi = pd.DataFrame(dados)
    coluna_sobrevi = sobrevi['survived']
    for valor in coluna_sobrevi:
        if valor == 1:
            total += 1
    return total

print("O total de sobreviventes foi",total_sobrevivente())   

def media_passageiros_idade():
    media_passa=pd.DataFrame(dados)
    media=(media_passa['age'].mean())

    return media

print(" A médis das idades dos pasageiros:",media_passageiros_idade())


def mulher_homens_abordo(dados):
    masculino=0
    feminino=0

    quanti_abordo = pd.DataFrame(dados)
    coluna_sexo = quanti_abordo['sex']
    for quantidade in coluna_sexo:
        if (quantidade=='male'):
            masculino=masculino+1
        elif(quantidade=='female'):
            feminino=feminino+1


    print("Quantidade de homens e mulheres abordo:",masculino,feminino)
mulher_homens_abordo(dados)
dados = sns.load_dataset('titanic')