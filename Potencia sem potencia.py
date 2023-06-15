'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.'''
for i in range(999):
    base = int(input('Digite o número da base: '))
    expo = int(input('Digite o número da base: '))

    resultado = 1
    negativo = 1

    for c in range(1):

        if expo == 0:
            print(f'\nO resultado para {base}^{expo} é 1, pois qualquer número elevado a {expo} resulta em 1(um)\n')

        elif expo == 1:
            print(f'O resultado para {base}^{expo} é {base}, pois qualquer número elevado a {expo} resulta em {base}\n')


        elif expo < 0:
            for neg in range(abs(expo)):
                resultado = resultado / base

        else:
            for pos in range(expo):
                resultado *= base

        print(f'\nResultado para: {base} ^ {expo} = {resultado}\n')

    escolha = str(input('Deseja realizar outro cálculo? [S]-Sim [N]-Não: \n').upper())
    print()
    if escolha == "N":
        break

# Comentário sobre a linha 20 - 25
''' A função abs() retorna o valor absoluto de um número sendo ele positivo,negativo ou complexo.
Basicamente um valor absoluto é independende de sua posição em um número, 
seu valor é a distância de 0 então -5,74 está a 5,74 casas distante de 0 então seu valor é 5,74

Logo após o resultado recebe o valor de resultado = resultado/base que é substituído pela divisão e atribuição "/="

No laço de repetição for neg in range(abs(expo)), o comando /= é utilizado para dividir o valor atual de resultado pelo valor da base. 
A cada iteração do loop, a variável resultado é atualizada com o resultado da divisão anterior dividido pela base. 
Isso é equivalente a realizar a operação de potenciação com expoente negativo.

Por exemplo, se base for 2 e expo for -3, o código realizará a seguinte operação:
resultado = 1
negativo = 1

for neg in range(abs(-3)):
    resultado /= base

# Resultado final: resultado = 1 / (2 * 2 * 2) = 1/8 = 0.125 - resultado = resultado / base


'''