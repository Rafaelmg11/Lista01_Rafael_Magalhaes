#Escreva um programa que peça ao usuario para inserir TRES números inteiro,some os DOIS primeiros e multiplique esse total pelo TERCEIRO.
#Exiba o resultado da operação com a seguinte mensagem: "O total é: [?]".
n1 = int (input('Digite o primeiro número: '))
n2 = int (input('Digite o segundo número: '))
n3 = int (input('Digite o terceiro número: '))
soma = n1 + n2
resultado = soma * n3
print("O total é",resultado)