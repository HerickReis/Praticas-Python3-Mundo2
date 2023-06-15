'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

aluno = 0
mais_alto = mais_baixo = 0
numero_alto = numero_baixo = 0
while aluno < 2:
    aluno += 1
    n = int(input(f'Numero do {aluno}° aluno: '))
    altura = int(input(f'altura do {aluno}° (em centimetros): '))
    print()

    if aluno == 1:
        mais_alto = altura
        mais_baixo = altura
        numero_alto = n
        numero_baixo = n

    else:
        if altura < mais_baixo:
            numero_baixo = n
            mais_baixo = altura

        if altura > mais_alto:
            numero_alto = n
            mais_alto = altura

print(f'''O numero do aluno mais baixo é {numero_baixo} e ele possui {mais_baixo}cm de altura, o numero do mais alto é {numero_alto} e ele possui {mais_alto}cm de altura.
''')