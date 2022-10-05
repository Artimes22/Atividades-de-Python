
import random
import time

from pyautogui import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('JOKENPÔ')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

jogador = int(input('Qual sua jogada? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print('-='*10)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-='*10)

if computador == 0: #computador joga PEDRA 
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE')
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('JOGADA INVALIDA')            

elif computador == 1: #computador joga PAPEL
    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('JOGADA INVALIDA')            

elif computador == 2: #computador joga TESOURA
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')            