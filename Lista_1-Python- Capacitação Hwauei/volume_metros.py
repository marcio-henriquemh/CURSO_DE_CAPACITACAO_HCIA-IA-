#Leia um valor de volume em metros cúbicos e apresente-o convertido em litros.
#A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume
#em metros cúbicos.

metros_cubicos=float(input("Informe o volume:"))
litros=metros_cubicos*1000

print("Volume em metros cubicos:",litros)