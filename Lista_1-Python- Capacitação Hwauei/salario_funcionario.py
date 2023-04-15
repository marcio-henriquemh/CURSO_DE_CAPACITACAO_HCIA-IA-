#Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
#prestação for maior que 20% do salário imprima: 'Empréstimo não concedido', caso
#contrário imprima: 'Empréstimo concedido'.
#20. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e
#mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à
#altura)

salario_trabalho=float(input("Salário do Funcionário"))
valor_prestacao=float(input("Informe o valor da prestação:"))
liberaca_emprestimo=salario_trabalho*0.20/100
if(valor_prestacao>liberaca_emprestimo):

    print("Emprestimo não liberado")
    print("prestação 20%",liberaca_emprestimo)
    print("salario funcionario:",salario_trabalho)
else:

    print("O emprestimo foi liberado")
    print("prestação 20%",liberaca_emprestimo)
    print("salario funcionario:",salario_trabalho)