lista = []
pares = []
ímpares = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Você quer continuar [S/N]: '))
    if resp in 'Nn':
        break
    
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)        
        
print('-=' *30)
print(f'A lista completa é {lista}')
print(f'A lista de numeros pares é {pares}')
print(f'A lista de numeros ímpares é {ímpares}')        