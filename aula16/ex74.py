from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Eu sorteei os seguintes valores ', end='' )
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')