'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

pais_a = int(80000)
taxa_anual_a = 0.03

pais_b = int(200000)
taxa_anual_b = 0.015

anos = 0
for i in range(1,1000000):

    if pais_a < pais_b:
        pais_a += pais_a * taxa_anual_a
        pais_b += pais_b * taxa_anual_b
        anos +=1 

if pais_a >= pais_b:
    print(f'''Foram necessários {anos} anos para que o pais_A se igualasse ou ultrapasasse o pais_B
Sendo assim o Pais_A atualmente conta com {pais_a:.0f} habitantes e o Pais_B conta com {pais_b:.0f} habitantes.''')

