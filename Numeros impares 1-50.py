'''Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.'''
from time import sleep
print('Os números ímpares são: ')
sleep(1)
for ni in range(0,51):
    if ni % 2 == 1 :
        print(ni)
