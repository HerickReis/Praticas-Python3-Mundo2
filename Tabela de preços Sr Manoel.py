'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50'''
cores = {
    'Azul' : "\033[34m",
    'Vermelho' : "\033[31m",
    'Verde' : "\033[32m",
    'Fim' : "\033[m",
    'Fundo Azul' : "\033["
}

produtos = 0
valor = 1.99
qntd = int(input('Qual a quantidade de produtos com o cliente? '))
print()
print("="*30)
print(f'Bem- Vindo a Lojas Quase Dois')
print("="*30)
print()
print(f'{cores["Verde"]} Tabela de preços {cores["Fim"]}')
while produtos < qntd:

    if qntd > 50:
        print(f'\n{cores["Vermelho"]} A quantidade informada ultrapassa o estoque disponível {cores["Fim"]}')
        print(f'\n{cores["Azul"]} Informe uma quantidade válida\n {cores["Fim"]}')
        qntd = int(input('Qual a quantidade de produtos com o cliente? '))
    else:
        produtos += 1
        print(f'{cores["Verde"]} {produtos} - R$: {valor * produtos:.2f} {cores["Fim"]}\n')
