'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações'''

nome_usuario = str(input('Insira seu nome de usuario: '))
senha = input('Crie uma senha: ')

for verificacao in range(3):

    if senha == nome_usuario:
        print(f'A senha é igual ao nome de usuário\nInsira uma senha diferente: ')
        print(f'Tentativa {verificacao+1}/3')
        senha = input('Crie uma senha: ')
    else:
        print('Senha válida')
        senha = input('Crie uma senha válida: ')