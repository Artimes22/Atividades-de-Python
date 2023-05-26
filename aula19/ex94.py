galera = []
pessoas = {}
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/f]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Apenas "M" ou "F"') 
    pessoas['idade']= int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0] 
        if resp in 'SN':
            break    
        print('ERRO! Responda apenas "S" ou "N"')              
    if resp == 'N':
        break      
print('-='*20)    
print(f'Ao todo foi cadastrado um total de {len(galera)} pessoas')    
media = soma / len(galera)
print(f'A medía de idade é de {media:5.2f} anos')
print('As mulheres cadastratas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print('')        
print('Lista de pessoas que estão com a idade acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}') 
            
print('>>>ENCERRADO<<<')            