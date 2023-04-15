#Peça ao usuário para digitar três valores inteiros e imprima a soma deles

#definindo valores

def numero_ao_quadrado(numero):
    numero_quadrado=int(input(numero))
    return pow(numero_quadrado,2)


numero_quadrado=numero_ao_quadrado("Informe o valor")
print("o valor ao quadrado foi:",numero_quadrado)
