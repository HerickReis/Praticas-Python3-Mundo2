'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n-ésimo termo.'''
n1 = 0
n2 = 1
c = n2 + n1
print(f'A sequência de Fibonnaci é:')
if n1 == 0 and n2 == 1:
    n1 = 0
    n2 = 1
    c = n2 + n1
    print(f'{n1} -> {n2} -> {c} ->',end=" -> ")

for s in range(2,):
    n1 = n2
    n2 = c
    c = n1 + n2
    print(f'{c}',end=" -> ")
print('FIM!')