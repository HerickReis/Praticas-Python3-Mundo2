'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.'''

for r in range(5+1):
    populacao_a = int(input('Digite a população do pais_A: '))
    taxa_crescimento_a = float(input('Qual a taxa de crescimento desse país? '))

    populacao_b = int(input('\nDigite a população do Pais_B: '))
    taxa_crescimento_b = float(input('Qual a taxa de crescimento desse país? '))

    anos_a = 0
    anos_b = 0

    for i in range(1,100000):

        if populacao_a < populacao_b :
            populacao_a += populacao_a + (populacao_a * taxa_crescimento_a / 100)
            populacao_b += populacao_b + (taxa_crescimento_b * taxa_crescimento_b / 100)
            anos_a += 1
            if populacao_a >= populacao_b:
                print(f'''\nForam necessários {anos_a} anos para o pais_A ter a mesma quantidade de habitantes ou maior que o Pais_B\n
                Atualmente o Pais_A conta com {populacao_a:.0f} habitantes, e o pais_B conta com {populacao_b:.0f} habitantes.''')
                break

        if populacao_b < populacao_a:
            populacao_b += populacao_b + (populacao_b * taxa_crescimento_b / 100)
            populacao_a += populacao_a + (populacao_a * taxa_crescimento_a / 100)
            anos_b += 1  
            if populacao_b >= populacao_a:
                print(f'''\nForam necessários {anos_b} anos para o pais_B ter a mesma quantidade de habitantes ou maior que o Pais_A\n
                Atualmente o Pais_B conta com {populacao_b:.0f} habitantes, e o pais_A conta com {populacao_a:.0f} habitantes.''')
                break

    resposta = str(input('Desja continuar? [s] ou [n]').upper) 
    print(f'Calculo {r+1}/5')
    if resposta == "N":
        break