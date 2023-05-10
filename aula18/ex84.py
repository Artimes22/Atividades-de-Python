pessoas = []
dados = []
pesoMaior = pesoMenor = 0
 
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesoMaior = pesoMenor = dados[1]
    else:
        if dados[1] > pesoMaior:
            pesoMaior = dados[1]
        if dados[1] < pesoMenor:
            pesoMenor = dados[1]        
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Você quer continuar: [S/N] '))
    if resp in 'nN':
        break

print(f'Foi cadastrado {len(pessoas)}')    
print(f'O maior peso foi de {pesoMaior}Kg. Peso de ', end=' ')
for p in pessoas:
    if p[1] == pesoMaior:
        print(f'{[p[0]]} ', end='')
print()        
print(f'O menor peso foi de {pesoMenor}Kg. Pesp de ', end=' ')
for p in pessoas:
    if p[1] == pesoMenor:
        print(f'{[p[0]]}', end=' ')
print()        