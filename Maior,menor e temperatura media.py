'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''
teste = False
maior = 0
menor = 0
qntd = 0
soma = 0
print('Digite "Ok" Para encerrar o programa.')
while teste != True:
    temp = float(input('Informe a temperatura: '))

    if temp != 99:
        qntd += 1

        if qntd == 1:
            menor = temp
            maior = temp
        else:
            if temp < menor:
                menor = temp
            if temp > maior:
                maior = temp
        soma += temp

    else:
        teste = True

if qntd > 0:
    media = soma / qntd
    print(f'A maior temperatura registrada foi {maior}°C, a menor foi {menor}°C, e a média das temperaturas foi {media}°C.')
else:
    print('Nenhuma temperatura válida foi registrada.')