'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

n1= int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

menor = min(n1,n2)
maior = max(n1,n2)
soma = n1+n2
for ni in range(menor, maior+1):
    print(ni)

print(f'''Os números digitados foram {n1 , n2}  sendo {maior} o maior e {menor} o menor
a soma entre eles é {soma}''')