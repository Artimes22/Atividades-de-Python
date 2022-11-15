import random
computador = random.randint(0, 10)

print('Sou seu Computador... Pensei em um número entre 0 e 10')
print('será que vecê consegue advinhar?')

acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if  jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez!')   
        elif jogador > computador:
            print('Menos... tente novamente!')     
print('Acertou com {} paltites' .format(palpite))        
