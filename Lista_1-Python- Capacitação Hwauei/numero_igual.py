#Faça um programa que receba dois números e mostre o maior. Se por acaso, os
#dois números forem iguais, imprima a mensagem 'Números iguais'.


numero_1=int(input("informe o valor 1:"))
numero_2=int(input("Informe o valor 2:"))
if(numero_1>numero_2):
        print("O valor maior é:",numero_1)
        print("E a diferença:",numero_1-numero_2)

elif(numero_2>numero_1):

        print("O valor maior é:",numero_2)
        print("E a diferença:",numero_2-numero_1)
else:

         print("São iguais:",numero_1 , numero_2)