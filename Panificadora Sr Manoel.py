'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00'''

preço_do_pão = float(input('Favor informe o preço do pão (unidade): '))
paes_cliente = int(input('Informe quantos pães o cliente está comprando: '))

qntd = 0

while qntd < paes_cliente:

    if qntd > 50:
        print('Quantidade acima do limite, Informe um valor menor.')
        paes_cliente = int(input('Informe quantos pães o cliente está comprando: '))
    
    else:
        qntd += 1
        print(f'{qntd} - R$: {qntd * preço_do_pão:.2f}\n')
