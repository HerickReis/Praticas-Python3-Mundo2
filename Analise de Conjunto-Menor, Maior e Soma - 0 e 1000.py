'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
-- Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

maior = 0
menor = 0
soma = 0 

numeros = int(input('Digite a quantidade de números a analisar: '))
for v in range(numeros):
    n = int(input(f'Digite o {v+1}° valor: '))
    if n >=0 and n <=1000 :
        if v == 0 :
            maior = n
            menor = n           
        elif v > 0 :
            if maior < n:
                maior = n
            if n < menor:
                menor = n
        soma += n
    else: 
        if n > 1000:
            print(f'\n O número digitado {n} está acima de 1000.')
            n = int(input(f'\nDigite o {v+1}° valor novamente: '))
            print()
            soma += n

        if n < 0:
            print(f'\n O número digitado {n} está abaixo de 0.')
            n = int(input(f'\nDigite o {v+1}° valor novamente: '))
            print()
            soma += n
print(f'\nVocê digitou {numeros} valores, o maior entre eles foi {maior} e o menor foi {menor}\nA soma entre eles foi {soma}\n')