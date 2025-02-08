#Escreva um programa que solicite um determinado número de dias,em seguida exiba o quanto esses dias equivalem em horas,minutos e segundos
dias = int (input('Digite um número de dia: '))
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60
print("")
print (dias,"dias equivalem á",horas,"horas,",minutos,"minutos e ",segundos,"segundos")
