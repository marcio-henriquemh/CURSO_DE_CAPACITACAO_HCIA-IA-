#Leia um número real. Se o número for positivo imprima a raiz quadrada. Do
#contrário, imprima o número ao quadrado

#12. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a
#raiz quadrada do número. Se o número for negativo, mostre uma mensagem
#dizendo que o número é inválido
#biblioteca
import math

#entrada de dados
numero=float(input("Informe o valor:"))

#condicoes
if(numero<0):
  
   print("O numero ao quadrado é:",math.pow(numero,2))
else:

#saída
  print("A raiz é:",math.sqrt(numero))

