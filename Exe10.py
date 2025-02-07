#Escreva um programa que pergunte quantos pedaço o bolo tem, em seguida pergunte ao usuario quantos pedaços ele comeu, calcule quantos pedaços ainda tem e exiba o resultado  com uma mensagem de livre escolha
bolo = int (input('Digite quantos pedaços tem seu bolo: '))
comeu = int (input('Digite quantos pedaços você comeu do bolo: '))
sobra = bolo - comeu
print("O bolo possuia",bolo,"pedaços,você comeu",comeu,", então sobrou",sobra,"pedaços restantes do bolo!")
print("Bom Apetite!!!")