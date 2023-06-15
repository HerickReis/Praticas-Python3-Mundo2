'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''
n = int(input('Digite um número inteiro: '))
c = 2
p = 0

while n < 2:
    print(f'{n} não é divisivel por nenhum número além dele mesmo\nInsira outro número.')
    n = int(input('Digite um número inteiro: '))

while c <= n:
    if n % c == 0:
        p += 1
        
    c += 1

if p == 1 :
    print(f'\nO número {n} é primo, pois foi divisivel {p} vezes.')

else:
    print(f'\nO número {n} não é primo, pois foi divisivel {p} vezes.')
