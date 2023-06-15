'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
limitando o fatorial a números inteiros positivos e menores que 16.'''
from time import sleep

for r in range(99999999999):
    resultado = 1

    print('Atenção, o programa aceita números inteiros até 16 e não aceita números negativos.')
    sleep(1.6)
    n = int(input('Digite um número inteiro para verificação: '))
    c = n
    if n == 0:
        break

    elif n <0 or n >16:
        if n <0 :
            print('\nNúmero negativo não aceito.\n')
        if n >16:
            print(f'\nO número inserido foi {n} e é maior que 16.\nInsira outro número.\n')
    else:
        for f in range(1, n+1):
            resultado *= f

    print(f'Obs: Números fatoriais são o mesmo que {n}...2x1 ou seja\n é a multiplicação de todos antecessores.')
    sleep(1.5)

print('{n}! = {resultado}')