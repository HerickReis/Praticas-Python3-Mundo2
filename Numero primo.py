'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

for r in range(9999999):
    p = 0

    numeros = int(input('\nDigite um número para análise (Insira 0 para sair) : '))
    if numeros == 0:
        break

    print()

    for n in range(1,numeros+1):

        if numeros % n == 0:
            print('\033[31m',end=" ")
            p += 1
            print(n,end=" ")

        else:
            print('\033[33m',end=" ")
            print(n,end=" ",)

    if p == 2:
        print(f'\nO número {numeros} é primo, pois foi divisivel {p} vezes.')
    else:
        print(f'\n O número {numeros} não é primo, pois foi divisivel {p} vezes.')