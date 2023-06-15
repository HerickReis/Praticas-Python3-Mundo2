'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

valor = 0
cds = 0
escolha = ""
while  escolha != True:
    print()
    print('-'*20)
    print('Menu')
    print()
    print('[1] - Adicionar Cd')
    print('[2] - Adicionar quantidade total de CDs')
    print('[3] - Realizar cálculo programa')

    print()
    print('-'*20)
    escolha = str(input('Qual opção deseja realizar? '))

    if escolha == "1":
        print('Adicionar Cd')
        
        add = float(input('Você quer adicionar um cd, Qual o valor deste cd? '))
        cds += 1
        valor += add
    
    elif escolha == "2":
        add = int(input('Ok! Insira a quantidade de CDs da coleção: '))     
        while cds < add:
            cds += 1
            valor_i = float(input(f'Insira o valor do {cds}° Cd: '))
            valor += valor_i
    
    elif escolha == "3":
        media = valor/cds
        print(f'\nVocê possui {cds} CDs em sua coleção\nO valor total de sua coleção de CDs é de R$: {valor}\nE a média por CD é de R$: {media}')
        escolha = True