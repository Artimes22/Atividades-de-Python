from random import randint
lista = []
jogos = []
cont = 0
print('-'*30)
print('      JOGA NA MEGA-SENA      ')
print('-'*30)
quant = int(input('Quantos jogos você quer sortear? '))
tot = 1
while tot <= quant:
    while True:    
        num = randint (1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break    

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont = 0
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)    
  
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    
print('-='*16)    