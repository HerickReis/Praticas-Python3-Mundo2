'''Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.'''
from time import sleep
print('='*20,'VERTICAL','='*20)
sleep(1)
for n in range(0,20+1):
    print(n)

sleep(3)
print('='*20,'HORIZONTAL','='*20)
sleep(1)
for n2 in range(0,20+1):
    print(n2,end=' ')