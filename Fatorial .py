'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

fatorial = int(input('Fatorial de: '))
# r recebe número e número recebe fatorial, O valor de cada variavel será independente
r = numero = fatorial

print(f'{fatorial}! = ',end=" ")

while numero != 2 :
    numero -= 1
    r *= numero
    print(f'{numero}',end=" . ")

print(f'1 = {r}')