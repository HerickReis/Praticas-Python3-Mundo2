'''Faça um programa que peça uma nota de 0 a 10. Mostre  uma mensagem caso o valor seja inválido
e continue pedindo até que o valor que o usuario informe seja válido'''

valor = int(input('Digite uum valor entre 0 e 10: '))

for r in range(10):

    if valor in range(0,10 +1):
        print('\nValor Válido!\n')
        print(f'\nTentativa {r+1}/10\n')
        valor = int(input('Digite outro valor para repetição: '))
        print()
        
 
    else :
        print('\nValor inválido tente novamente.\n')
        print(f'Tentativa {r+1}/10\n')
        valor =  int(input('Digite um valor entre 0 e 10: '))                                                                                                                                                                                                                                                  