'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n-ésimo termo escolhido pelo usuario.'''

seq = int(input('Escolha o termo a ser calculado: '))

n1 = 0
n2 = 1
c = 0

if n1 == 0 and n2==1:
    n1 = 0
    n2= 1
    c = n1 + n2
    print(f'{n1} -> {n2} -> {c}',end="-> ")

for s in range(seq):
    n1 = n2
    n2 = c
    c = n1 + n2
    print(f'{c}',end=" -> ")