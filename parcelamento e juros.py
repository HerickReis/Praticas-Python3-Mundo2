'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, 
quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:

Valor da Dívida     Valor dos Juros   Quantidade de Parcelas      Valor da Parcela
R$ 1.000,00             0                  1                       R$  1.000,00
R$ 1.100,00             100                3                       R$    366,00
R$ 1.150,00             150                6                       R$    191,67
'''


valor_divida = float(input('Digite o valor da dívida: '))
juros_i = 10

juros_totais = 0

valor_atual = 0
parcelas = 0
valor_parcelas = 0
print(f'''\nValor da Dívida          Valor dos Juros          Quantidade de parcelas                 Valor da parcela
    R$: {valor_divida}                        0                               {parcelas+1}                     {valor_divida}''')
while parcelas < 12:

    juros_totais = valor_divida * (juros_i/100)
    valor_atual = valor_divida + juros_totais

    parcelas += 3

    valor_parcelas = valor_atual / parcelas
    print(f'    R$: {valor_atual:.2f}                     {juros_totais}                              {parcelas}                    {valor_parcelas:.2f}')
    juros_i += 5