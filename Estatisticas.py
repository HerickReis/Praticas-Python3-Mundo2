'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). 
Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

cidades = 0
cidades_estudadas = 5
maior = menor = 0
cidade_maior = cidade_menor = ""

cidade1_codigo = 1
cidade1_veiculos = 1500
cidade1_acidentes = 30

cidade2_codigo = 2
cidade2_veiculos = 2000
cidade2_acidentes = 45

cidade3_codigo = 3
cidade3_veiculos = 1800
cidade3_acidentes = 20

cidade4_codigo = 4
cidade4_veiculos = 2500
cidade4_acidentes = 50

cidade5_codigo = 5
cidade5_veiculos = 1700
cidade5_acidentes = 15

media = cidade1_veiculos + cidade2_veiculos + cidade3_veiculos + cidade4_veiculos + cidade5_veiculos
veiculos_menos_2k = 0

while cidades <= cidades_estudadas:
    cidades += 1

    if cidades == 1:
        maior = cidade1_acidentes
        menor = cidade1_acidentes

    else:

        # verificação maior Cidade 1
        if cidade1_acidentes > maior:
            maior = cidade1_acidentes
            cidade_maior = "Cidade 1"

        # verificação maior cidade 2
        if cidade2_acidentes > maior: 
            maior = cidade2_acidentes
            cidade_maior = "Cidade 2"

        # verificação maior cidade 3
        if cidade3_acidentes > maior:
            maior = cidade3_acidentes
            cidade_maior = "Cidade 3"

        # verificação maior cidade 4     
        if cidade4_acidentes > maior:
            maior = cidade4_acidentes
            cidade_maior = "Cidade 4"

        # verificação maior cidade 5
        if cidade5_acidentes > maior:
            cidade_maior = "Cidade 5"

        # verificação menor cidade 1
        if cidade1_acidentes < menor:
            menor = cidade1_acidentes
            cidade_menor = "Cidade 1"

        # verificação menor cidade 2
        if cidade2_acidentes < menor:
            menor = cidade2_acidentes
            cidade_menor = "Cidade2"

        if cidade3_acidentes < menor:
            menor = cidade3_acidentes
            cidade_menor = "Cidade 3"

        if cidade4_acidentes < menor:
            menor = cidade4_acidentes
            cidade_menor = "Cidade 4"

        if cidade5_acidentes < menor:
            menor = cidade5_acidentes
            cidade_menor = "Cidade 5"

if cidade1_veiculos < 2000:
    veiculos_menos_2k += cidade1_acidentes
        
if cidade2_veiculos < 2000:
        veiculos_menos_2k += cidade2_acidentes

if cidade3_veiculos < 2000:
    veiculos_menos_2k += cidade3_acidentes

if cidade4_veiculos < 2000:
    veiculos_menos_2k += cidade4_acidentes

if cidade5_veiculos < 2000:
    veiculos_menos_2k += cidade5_acidentes

print(f'''O menor indice de acidentes de transito pertence a {cidade_menor} com {menor} indices de acidentes

O maior indice pertence a {cidade_maior} com {maior} indice de acidentes

A media de veiculos de todas cidades é {media / cidades_estudadas}

A media de acidente de transito em cidades com menos de 2000 (dois mil) veículos é de {veiculos_menos_2k / cidades_estudadas}''')