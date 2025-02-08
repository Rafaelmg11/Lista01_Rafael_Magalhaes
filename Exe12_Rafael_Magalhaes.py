#Escreva um programa que pergunte o valor total da conta, em seguida pergunte quantos clientes existem,divida a conta pelos clientes e exiba o quanto cada cliente deve pagar 
#seguida da mensagem "Cada cliente deve pagar: " [x valor]

conta = float (input('Digite o valor da conta: '))
clientes = int (input('Digite o números de clientes à dividir a conta: '))
resultado = conta/clientes
print("Cada cliente irá pagar : R$",resultado)