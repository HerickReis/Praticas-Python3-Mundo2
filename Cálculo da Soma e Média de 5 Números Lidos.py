'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''
soma = 0
inicio = 0
fim = 5
numeros_info = []
media = 0
for n in range(inicio,fim+1):
    numeros = float(input(f'Digite o {n+1}° número: '))
    soma += numeros
    media = soma / fim
    numeros_info.append(numeros)

print(f'Os numeros informados foram',numeros_info ,end=' ',)
print(f'E as somas entre eles resultam em {soma:.2f}\n a média resulta em {media:.2f}.')