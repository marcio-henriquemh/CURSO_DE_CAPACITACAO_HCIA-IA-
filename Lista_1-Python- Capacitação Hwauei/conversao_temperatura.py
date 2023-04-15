#Leia uma temperatura em graus Celsius e apresente-a convertida em graus
#Fahrenheit. A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo C a
#temperatura em Celsius e F a temperatura em Fahrenheit

grau_cel=float(input("Informe a temperatura em graus celcius:"))
convertendo_fahrenheit=5*(grau_cel * 9/5) + 32.0


print(f"A temperatura em Fahrenheit é {convertendo_fahrenheit:.2f}°F")