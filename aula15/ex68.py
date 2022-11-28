import random

vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIn':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).upper() .strip() [0]
    print(f'Você jogou {jogador} e o computador {computador}, total de {total}. ', end='')
    print('Deu PAR' if total %2 == 0 else 'Deu ÍMPAR')

    if tipo == 'P':
        if total %2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break    
    elif tipo == 'I':    
        if total %2 == 1 :
                print('Você VENCEU! ')
                vitoria += 1
        else:
             print('Você PERDEU! ') 
             break
    print('Vamos jogar novamente ...')
print(f'GAME OVER,Você ganhou {vitoria} vezes')               