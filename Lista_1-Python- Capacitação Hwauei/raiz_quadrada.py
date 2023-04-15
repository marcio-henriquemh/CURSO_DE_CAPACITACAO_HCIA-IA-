#12. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a
#raiz quadrada do número. Se o número for negativo, mostre uma mensagem
#dizendo que o número é inválido
#biblioteca
import math

#entrada de dados
numero=float(input("Informe o valor:"))

#condicoes
while(numero<0):
    print("Valor tem que ser positivo")
    numero=float(input("Informe o valor:"))

else:

#saída
    print("A raiz é:",math.sqrt(numero))
