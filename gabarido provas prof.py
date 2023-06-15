from time import sleep

gabarito = {}
q = 1
t_questoes = 0

prova = "S"
aluno = acertos_totais = 0

print('Para interromper o programa insira o numero da questao 0')
while q != 0:
    questao = int(input('\nInsira o numero da questão: ').strip())
    
    if questao == 0:
        q = 0
    t_questoes += 1

while prova != "N":
    questoes = 00
    acertos = erros = 0
    aluno += 1
    while questoes < t_questoes:
        questoes += 1
        resposta = str(input(f'\nQual sua resposta para a questao {questoes}? ').upper())

        if resposta == gabarito.get(questoes):
            acertos_totais += 1
            acertos += 1

        else:
            erros +=1

    prova_2 = str(input('\nIniciar nova prova [S/N]? ').upper())

    if prova_2 == "S":
        print(f'\nO {aluno}° aluno obteve {acertos} acertos e {erros} erros\n')
        sleep(2)
        prova = "S"

    else:
        print(f'\nO {aluno}° aluno obteve {acertos} acertos e {erros} erros\n a media de notas da turma foi de {acertos_totais/aluno :.2f}\n')
        prova = "N"