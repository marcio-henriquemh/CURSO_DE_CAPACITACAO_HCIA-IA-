import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from sklearn.preprocessing import PolynomialFeatures

# importando os dados
dados = pd.read_csv('/home/marciohenrique/Capacitação em IA-Huawei/Algoritmos de Machine Learning/Regressao_Polinomial/regre_polinomial.csv')
X = dados.iloc[:, 1:2].values
y = dados.iloc[:, 2].values

# regressão polinomial
def funcao_polinomial(X, y, d):
    from sklearn.preprocessing import PolynomialFeatures
    polynomialFeatures = PolynomialFeatures(degree=d)
    X_polinomial = polynomialFeatures.fit_transform(X)

    from sklearn.linear_model import LinearRegression
    polyLinearRegress = LinearRegression()
    polyLinearRegress.fit(X_polinomial, y)

    return X_polinomial, polyLinearRegress

# plotando o gráfico com a regressão polinomial
def grafico_polinomial(Xpontos, ypontos, regressor):
    Xmin, Xmax = np.min(Xpontos), np.max(Xpontos)
    Xlinha = np.linspace(Xmin, Xmax, 100).reshape(-1, 1)

    # obtem a linha de regressão polinomial
    X_polinomial = regressor[0]
    polyLinearRegress = regressor[1]
    ylinha = polyLinearRegress.predict(PolynomialFeatures(degree=X_polinomial.shape[1]-1).fit_transform(Xlinha))

    # plota os pontos e a linha de regressão polinomial
    plt.scatter(Xpontos, ypontos, color='red')
    plt.plot(Xlinha, ylinha, color='blue')
    plt.title("Comparando pontos reais com a reta produzida pela regressão polinomial")
    plt.xlabel("Experiência em anos")
    plt.ylabel("Salário")
    plt.show()

# Dividindo o conjunto de dados em conjunto de treinamento e conjunto de teste
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# chamando a regressao polinomial e plotando o gráfico
regressor = funcao_polinomial(X_train, y_train, 3)
grafico_polinomial(X_train, y_train, regressor)
