item = ' '
preco = total = totmil = menor = cont = 0
print('='*30)
print('LOJA')
print('=' *30)

while True:
    item = str(input('O que você vai comprar? '))
    preco = float(input('Qual o preço do item? '))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco            
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer comprar mais? [S/N]')).upper() .strip() [0]
    if continuar == 'N':
        break

print(f'Quantidade de produtos a cima de 1000 reais: {totmil} ')
print(f'total gasto R${total:.2f}')
print(f'O produto masi barato custa R${menor:.2f}')