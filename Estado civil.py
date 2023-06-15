'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

 
nome = str(input('Digite seu nome: ').strip().title())
idade = int(input('Digite sua idade: ').strip())
salario = float(input('Digite seu salário: ').strip())
sexo = str(input('[M] - Masculino\n[F] - Feminino\nInsira seu sexo: ').upper().strip())

print('\nInforme seu estado civil')
estado_civil = str(input('[S] - Solteiro\n[C] - Casado\n[V] - Viúvo\n[D]-Divorciado\nEscolha: ').upper().strip())

for validacao in range(6):
    
    if  len(nome) < 3:
        print('Nome inválido!\nDigite um nome válido.')
        nome = str(input('Digite seu nome: ').strip().title())

    if idade  < 0 and idade >=150:
        print('Idade inválida\nPor favor insira um idade válida.')
        idade = int(input('Digite sua idade: ').strip())
        
    if salario < 0:
        print(f'Salário inválido\nPor favor insira um saláio válido.')
        salario = float(input('Digite seu salário: ').strip()) 

    if sexo == "M":
        sexo = "Masculino"
    elif sexo == "F":
        sexo = "Feminino"
    else:
        print('Sexo inválido\nPor favor insira um sexo válido.')
        sexo = str(input('[M] - Masculino\n[F] - Feminino\nInsira seu sexo: ').upper().strip())

    if estado_civil == "S":
        estado_civil = "Solteiro"
    elif estado_civil == "C":
        estado_civil = "Casado"
    elif estado_civil == "V":
        estado_civil = "Viúvo"
    elif estado_civil == "D":
        estado_civil = "Divorciado"
    else:
        estado_civil = str(input('Escolha uma opção válida '))

    break

print("="*20)
print(f'{nome}\n{idade} Anos\nR$: {salario}\n{sexo}\n{estado_civil}')