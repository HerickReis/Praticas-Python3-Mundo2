'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''
import datetime

data_contratacao = 1995
salario_inicial = float(input('Salario inicial: '))
percentual_de_aumento = 1.5

ano_atual = datetime.datetime.now().year
tempo_de_trabalho = ano_atual - data_contratacao

tempo_de_trabalhado_total= 1
salario_atual = salario_inicial

while tempo_de_trabalhado_total <= tempo_de_trabalho:
    salario_atual += salario_atual * (percentual_de_aumento / 100)
    percentual_de_aumento *= 2

    tempo_de_trabalhado_total += 1

print(f'Com {tempo_de_trabalhado_total} anos de trabalho você recebe hoje um salario de R$: {salario_atual}')