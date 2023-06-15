'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''
soma = 0
menor = 0
maior = 0

valores = int(input('Quantos valores deseja verificar? '))

for v in range(valores):
    n = int(input(f'Digite o {v+1}° valor: '))
    
    if valores > 1:
        if v == 0:
            maior = n
            menor = n

        elif v > 0:
            if n > maior :
                maior = n
            if n < menor:
                menor = n              
        
        soma += n
    else:
        print(f'\nVocê inseriu apenas um valor. N°:{n}\n')

print(f'\nA soma dos {valores} valores inseridos foi igual a {soma}.\nO menor valor inserido foi {menor} e o maior foi {maior}\n')