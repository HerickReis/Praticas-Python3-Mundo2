'''faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''
resultado = 1

for r in range(99999):

    resultado = 1

    n = int(input('Digite o número para verificar: '))
    if n == 0 :
        print()
        break

    for s in range(1,n+1):
        resultado *= s

    print(f'\nResultado:\n{n}! = {resultado}\n')