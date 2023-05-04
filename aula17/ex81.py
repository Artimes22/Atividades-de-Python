lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Você quer continuar [S/N]: '))
    if r in 'Nn':
        break
lista.sort(reverse=True)    

print('-='*30)

print(f'Voce informou {len(lista)} valores')
print(f'Os valores informados em ordem decrecente são: {lista}')    
 
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não foi informado na lsita')    