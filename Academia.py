'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''
'''
Passo a Passo

1 - Fazer variáveis que peçam código,altura, peso, e uma para calcular medias
2 - criar variáveis para receber o mais alto, mais gordo, mais baixo e mais magro
3 - criar o loop para pedir as informações n vezes, e se o usuario digitar 0 o loop é encerrado e o calculo é feito
4 - exibir o mais alto, o mais baixo, o mais gordo e o mais magro'''

codigo = 1
clientes = 0
peso = 0
peso_gordo = peso_magro = 0
mais_alto = mais_baixo = 0
codigo_m = codigo_g = 0
codigo_alto = codigo_baixo = 0
while codigo != 0:
    codigo = int(input('\nInforme seu código: '))

    if codigo == 0:
        break

    nome = str(input('Digite seu nome: '))
    altura = float(input(f'{nome} qual sua altura? '))
    peso = float(input(f'{nome} informe seu peso: '))
    print()

    if clientes == 0:
        peso_gordo = peso
        peso_magro = peso
        codigo_g = codigo
        codigo_m = codigo
        mais_alto = altura
        mais_baixo = altura
        codigo_baixo = codigo
        codigo_alto = codigo

    else:
        if peso > peso_gordo:
            codigo_g = codigo
            peso_gordo = peso

        if peso < peso_magro:
            codigo_m = codigo
            peso_magro = peso

        if altura > mais_alto:
            codigo_alto = codigo
            mais_alto = altura

        if altura < mais_baixo:
            codigo_baixo = codigo
            mais_baixo = altura

    clientes += 1

print(f'''O cliente com o codigo {codigo_baixo} possui {mais_baixo}cm de altura e é o mais baixo, O cliente com o codigo {codigo_alto} tem {mais_alto}cm de altura e é o mais alto.
O cliente com o codigo {codigo_g} tem {peso_gordo}kg e é o mais gordo, O cliente como codigo {codigo_m} tem {peso_magro}kg e é o mais magro''')
