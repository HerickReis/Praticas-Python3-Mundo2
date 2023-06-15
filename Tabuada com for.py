'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:'''
for r in range(99999):
    numero = float(input('Tabuada do: '))
    inicio = int(input('Começa em: '))
    limite = int(input('Termina em: '))

    print(f'Tabuada de {numero}')

    for t in range(inicio,limite+1):
        print(f'{numero} X {t} = {numero*t:.3f}')
    resultado = str(input('Deseja fazer outra tabuada? [S]-Sim [N]-não: ').upper())
    if resultado == "N":
        break