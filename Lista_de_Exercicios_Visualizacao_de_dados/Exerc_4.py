#importando as bibliotecas
import seaborn as sns
import statistics
import matplotlib.pyplot as plt 
import pandas as pd

dados = sns.load_dataset('titanic')

#definindo a função
def mulher_homens_abordo():
    masculino = 0
    feminino = 0

    quanti_abordo = pd.DataFrame()
    coluna_sexo = dados['sex']
    for quantidade in coluna_sexo:
        if quantidade == 'male':
            masculino += 1
        elif quantidade == 'female':
            feminino += 1

    figura, fm = plt.subplots(figsize=(2, 2))

    fm.plot( feminino, color='r', linestyle='-', label='Label 1', marker='o', markevery=5)
    fm.plot(masculino,  color='b', linestyle='-', label='Label 1', marker='o', markevery=5)
    fm.set_title("Gráfico da quantidade de homens e mulheres a bordo")
    fm.set_xlabel("Eixo x", size=22)
    fm.set_ylabel("Eixo y", size=22)
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()
    print("Quantidade de homens e mulheres a bordo:", masculino, feminino)

mulher_homens_abordo()
