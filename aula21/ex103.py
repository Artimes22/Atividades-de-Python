#----------------------------FICHA DE JOGADOR COM NOME E NÚMERO DE GOLS---------------------------#

def ficha(jogador = '<Desconhecido>', gols = 0):
    print(f'O jogador {jogador} fez {gols} gosls no campeonato')
    
j = str(input('Nome do jogador: '))
g = str(input('Gols marcados: '))   

if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)    
            