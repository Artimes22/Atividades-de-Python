time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador: '))
    tot  = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Qunatos gols o {jogador["nome"]} fez na {c +1}ª partida:  ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
    
print('='*40)    
for k, v in enumerate(time):
    print(f'{k:>5}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print('')    
print('='*40)
print('-='*20)    
 