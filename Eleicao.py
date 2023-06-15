'''faça um programa que deve-rá calcular e exibir várias informações relacionadas a uma eleição presidencial com quatro candidatos. 
Os votos são registrados por meio de códigos específicos, e cada código corresponde a uma opção de voto. Os códigos utilizados são os seguintes:

1: Voto para o primeiro candidato (José, por exemplo)
2: Voto para o segundo candidato (João, por exemplo)
3: Voto para o terceiro candidato (Maria, por exemplo)
4: Voto para o quarto candidato (Ana, por exemplo)
5: Voto nulo
6: Voto em branco
O programa deve realizar as seguintes tarefas:

Registrar os votos e calcular o total de votos para cada candidato.
Calcular o total de votos nulos.
Calcular o total de votos em branco.
Calcular a percentagem de votos nulos em relação ao total de votos.
Calcular a percentagem de votos em branco em relação ao total de votos.
Para finalizar o conjunto de votos, é fornecido o valor zero.'''

codigos = True
candidatos = ("Ludrao","Jacinto Mesonaro","Ciroki Gripado","Simanca Tablet","Padre Kalminho",)

ludrao = mesonaro = ciroki = simanca = padre = 0
nulo = voto_branco = votos_totais = 0

while codigos == True:
    print('-'*20)
    print('Candidatos')
    print('-'*20)
    print('[1] - Escolher candidato')
    print('[2] - Voto Nulo')
    print('[3] - Voto em branco')
    print('[0] - Sair')
    opcao = str(input('Opção: ').strip()) 

    if opcao == "1":
        print(f'\n[1] - {candidatos[0]}')
        print(f'[2] - {candidatos[1]}')
        print(f'[3] - {candidatos[2]}')
        print(f'[4] - {candidatos[3]}')
        print(f'[5] - {candidatos[4]}')
        voto = str(input('Escolha seu candidato: ').strip())
        votos_totais += 1
        print()

        if voto == "1":
            ludrao += 1
        elif voto == "2":
            mesonaro += 1
        elif voto == "3":
            ciroki += 1
        elif voto == "4":
            simanca += 1
        elif voto == "5":
            padre += 1
        else:
            print('\nCandidato Inválido,Informe um candidato de acordo com a lista acima.')
            print(f'\n[1] - {candidatos[0]}')
            print(f'[2] - {candidatos[1]}')
            print(f'[3] - {candidatos[2]}')
            print(f'[4] - {candidatos[3]}')
            print(f'[5] - {candidatos[4]}')
            voto = str(input('Escolha seu candidato: ').strip())
            print()

    elif opcao == "2":
        print('Você votou nulo.')
        nulo += 1
        votos_totais += 1

    elif opcao == "3":
        print('Você votou em branco')
        voto_branco += 1
        votos_totais += 1

    elif opcao == "0":
        codigos = False

    else:
        print('Opcao inválida, Escolha uma opção válida.')

porcentagem_nulos = (nulo / votos_totais) * 100
porcentagem_brancos = (voto_branco / votos_totais) * 100

vencedor = ""

if ludrao > mesonaro and ludrao > ciroki and ludrao > simanca and ludrao > padre:
    vencedor = candidatos[0]

elif mesonaro > ludrao and mesonaro > ciroki and mesonaro > simanca and mesonaro > padre:
    vencedor = candidatos[1]

elif ciroki > ludrao and ciroki > mesonaro and ciroki > simanca and ciroki > padre:
    vencedor = candidatos[2]

elif simanca > ludrao and simanca > mesonaro and simanca > ciroki and simanca > padre:
    vencedor = candidatos[3]

elif padre > ludrao and padre > mesonaro and padre > ciroki and padre > simanca:
    vencedor = candidatos[4]
    

print(f'''O total de votos foram:
{candidatos[0]} : {ludrao}
{candidatos[1]} : {mesonaro}
{candidatos[2]} : {ciroki}
{candidatos[3]} : {simanca}
{candidatos[4]} : {padre}

Votos em Branco : {voto_branco}
Votos Nulos : {nulo}

Houve um total de {votos_totais} votos.

Resultado: {vencedor} venceu com {max(ludrao,mesonaro,ciroki,simanca,padre)} votos
O percentual de votos nulos foi de: {porcentagem_nulos:.2f}%
O percential de votos em branco foi de: {porcentagem_brancos:.2f}%''')