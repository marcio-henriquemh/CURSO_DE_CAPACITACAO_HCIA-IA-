#Lia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em
#m/s (metros por segundo). A fórmula de conversão é: M = k / 3.6, sendo K a
#velocidade em km/h e M e m/s.

velocidade=float(input("Informe a velocidade:"))
velocidade_convertida_metro_s=velocidade/3.6

print("Velocidade em metros por segundo:",velocidade_convertida_metro_s)