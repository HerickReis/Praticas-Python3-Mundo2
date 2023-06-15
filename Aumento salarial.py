'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''
import datetime

data_de_contratacao = 1995
salario_inicial = 1000
aumento_anterior = 1.5

atual = datetime.datetime.now().year
tempo_trabalhado = atual - data_de_contratacao

anos_de_trabalho = 1
salario_atual = salario_inicial

while anos_de_trabalho <= tempo_trabalhado:
    salario_atual += salario_atual * (aumento_anterior / 100)
    aumento_anterior *= 2

    anos_de_trabalho += 1
    

print(tempo_trabalhado)
print(salario_atual)
