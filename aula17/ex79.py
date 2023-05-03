numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar...')    
    r = str(input('Você quer continuar [S/N]: '))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você informou os valores {numeros}')    