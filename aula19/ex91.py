from random import randint
import time
from operator import itemgetter

jogo = {'Jogador1': randint(1, 20),
        'Jogador2': randint(1, 20),
        'Jogador3': randint(1, 20),
        'Jogador4': randint(1, 20)}
ranking = []
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v}')
    time.sleep(0.7)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 
time.sleep(1)   
print('')
print('O ranking ficou: ')
print('')   
time.sleep(1)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(0.5)   