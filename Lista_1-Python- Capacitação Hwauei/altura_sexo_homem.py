#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e
#mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à
#altura):

altura=float(input("Informe a altura:"))
sexo=str(input("Informe o sexo:"))


peso_ideal_homem=(72.7*altura)-58
peso_ideal_mulher=(62.1*altura)-44.7

if(sexo=="H"):
    print("Peso dea da homem:",peso_ideal_homem)

elif(sexo=="M"):

    print("Peso ideal mulher:",peso_ideal_mulher)