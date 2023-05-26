jogador = {}
partidas = []
jogador['nome'] = str(input('Qual o nome do jogador: '))
tot  = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'Qunatos gols o {jogador["nome"]} fez na {c +1}ª partida:  ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*20)
print(jogador)
print('-='*20)

for k, v in jogador.items():
    print(f'  -{k} tem o valor de {v}')    

print('-='*20)    
print(f'O {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i , v in enumerate(jogador['gols']):
    print(f'    => Na partida {i} ele marcou {v} gols')
print(f'Foi um total de {jogador["total"]} gols marcados durante o campeonato ')    