import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
#importando os dados

dados=pd.read_csv('/home/marciohenrique/Capacitação em IA-Huawei/Algoritmos de Machine Learning/Regressao_Polinomial/regre_polinomial.csv')
X = dados.iloc[:, 1:2].values
y = dados.iloc[:, 2].values

#Dividindo o conjunto de dados em conjunto de treinamento e conjunto de teste
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



# Ajustando a regressão linear ao conjunto de dados
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# REsultado da REgressão LInear
def viz_linear():
    plt.scatter(X, y, color='blue')
    plt.plot(X, lin_reg.predict(X), color='black')
    plt.title('Gráfico da Regressão Linear')
    plt.xlabel('Posição de Experiencia')
    plt.ylabel('Salário')
    plt.show()
    return
viz_linear()
