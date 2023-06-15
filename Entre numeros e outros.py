'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.'''

'''ni = False
entre_0_25 = entre_26_50 = 0
entre_51_75 = entre_76_100 = 0

# Opção 1:
while ni == False:
    nmrs = int(input('Digite um número inteiro (digite -1 para encerrar o programa): '))

    if nmrs >= 0 and nmrs <=25:
        entre_0_25 += 1
    
    if nmrs >= 26 and nmrs <=50:
        entre_26_50 += 1

    if nmrs >= 51 and nmrs <=75:
        entre_51_75 += 1
    
    if nmrs >= 76 and nmrs <=100:
        entre_76_100 += 1

    if nmrs <0:
        ni = True

print'''#(f'''Foram inseridos {entre_0_25} numeros entre [0-25]
#Foram inseridos {entre_26_50} numeros entre [26-50]
#Foram inseridos {entre_51_75} numeros entre [51-75]
#Foram inseridos {entre_76_100} numeros entre [76-100]''')

ni = False
entre_0_25 = entre_26_50 = 0
entre_51_75 = entre_76_100 = 0

# Opção 2
while ni == False:
    nmrs = int(input('Digite um número inteiro (digite -1 para encerrar o programa): '))

    if nmrs in range(0,25):
        entre_0_25 += 1
    
    if nmrs in range(26,50):
        entre_26_50 += 1

    if nmrs in range(51,75):
        entre_51_75 += 1
    
    if nmrs in range(76,100):
        entre_76_100 += 1

    if nmrs <0:
        ni = True

print(f'''Foram inseridos {entre_0_25} numeros entre [0-25]
Foram inseridos {entre_26_50} numeros entre [26-50]
Foram inseridos {entre_51_75} numeros entre [51-75]
Foram inseridos {entre_76_100} numeros entre [76-100]''')