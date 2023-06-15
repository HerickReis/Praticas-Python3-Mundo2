'''Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
12376489
=> 98467321'''

t = 1
while t == 1:

    numero = int(input('Informe um número inteiro: '))
    i = numero+1
    while i != 1:
        i -= 1
        print(i,end=" ")
    
    nv = str(input('\nDeseja tentar novamente [S/N]? ').upper())
    if nv == 'N':
        t = 0