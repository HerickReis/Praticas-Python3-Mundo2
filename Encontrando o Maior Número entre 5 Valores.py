'''Faça um programa que leia 5 números e informe o maior número.'''
maior = 0
menor = 0
for n in range(1,5+1):
    print(n)
    if n ==1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'O menor numero é {menor} e o maior é {maior}.')