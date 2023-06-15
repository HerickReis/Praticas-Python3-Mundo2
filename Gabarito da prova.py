'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.'''
from time import sleep

gabarito = {
1:"A",
2:"B",
3:"C",
4:"D",
5:"E",
6:"E",
7:"D",
8:"C",
9:"B"
}

prova = "S"
aluno = acertos_totais = 0

while prova != "N":
    questoes = 00
    acertos = erros = 0
    aluno += 1
    while questoes < 9:
        questoes += 1
        resposta = str(input(f'Qual sua resposta para a questao {questoes}? ').upper())

        if resposta == gabarito.get(questoes):
            acertos_totais += 1
            acertos += 1

        else:
            erros +=1

    prova_2 = str(input('Iniciar nova prova [S/N]? ').upper())

    if prova_2 == "S":
        print(f'\nO {aluno}° obteve {acertos} e {erros} erros\n')
        sleep(2)
        prova = "S"

    else:
        print(f'\nO {aluno}° obteve {acertos} e {erros} erros\n a media de notas da turma foi de {acertos_totais/aluno}\n')
        prova = "N"