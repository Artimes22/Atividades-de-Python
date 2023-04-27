num = (int(input('informe um valor: ')),
       int(input('informe outro valor: ')),
       int(input('informe mais um valor: ')),
       int(input('informe o ultimo valor: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na prosição {num.index(3) + 1}')
else:
    print('O número 3 não foi digitado em nenhuma posição')    
print('Os valores pares digitados são: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ') 
    