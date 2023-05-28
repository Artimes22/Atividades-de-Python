#--------------------SORTEIO DE NÚMEROS E A SOMA DOS NÚMEROS PARES-------------------#

from random import randint
import time

def sorteia (lista):
    print('Sorteando 5 valores da lista ...')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end=' ', flush=True)
        time.sleep(0.3)
    print('\nPRONTO! ')    

def somaPar(lista):
    soma = 0
    for valor in lista:        
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valroes pares de {lista} temos {soma}')            

números = []
sorteia(números)
somaPar(números)
