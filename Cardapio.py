'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

pedidos = False

cachorro_quente = bauru_simples = bauru_com_ovo = 0
cheeseburger = refrigerante = hamburguer = 0
preco_cq = preco_bau_s = preco_bau_c_o = preco_chess = preco_refri = preco_hamb = 0
cliente = -1
while pedidos != True:
    print('''
Produto             Código         Preço
Cachorro Quente     100         R$ 1,20
Bauru Simples       101         R$ 1,30
Bauru com ovo       102         R$ 1,50
Hambúrguer          103         R$ 1,20
Cheeseburguer       104         R$ 1,30
Refrigerante        105         R$ 1,00''')
    cliente = int(input('\nDigite o código do produto desejado (digite 0 para encerrar o pedido): '))

    if cliente == 0:
        print(f'''Produto                           Código                      Quantidade                  Preço
Cachorro Quente                     100                         {cachorro_quente}                           {preco_cq}
Bauru Simples                       101                         {bauru_simples}                             {preco_bau_s}         
Bauru com Ovo                       102                         {bauru_com_ovo}                             {preco_bau_c_o}
Hamburguer                          103                         {hamburguer}                             {preco_hamb}
Cheeseburguer                       104                         {cheeseburger}                             {preco_chess}
Refrigerante                        105                         {refrigerante}                             {preco_refri}         ''')
        break

    quantidade = int(input('Informe a quantidade: '))

    if cliente == 100:
        cachorro_quente += quantidade
        preco_cq = quantidade * 1.20

    elif cliente == 101:
        bauru_simples += quantidade
        preco_bau_s = quantidade * 1.30

    elif cliente == 102:
        bauru_com_ovo += quantidade
        preco_bau_c_o = quantidade * 1.50
    
    elif cliente == 103:
        hamburguer += quantidade
        preco_hamb = quantidade * 1.20

    elif cliente == 104:
        cheeseburger += quantidade
        preco_chess = quantidade * 1.30

    elif cliente == 105:
        refrigerante += quantidade
        preco_refri = quantidade * 1.00

    else:
        print('\nProduto não encontrado\n Escolha um produto válido')
        cliente = int(input('Digite o código do produto desejado: '))
        quantidade = int(input('Informe a quantidade: '))