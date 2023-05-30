from uteis import numeros
#Programa principal
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O valor fatorial de {num} é igual a {fat}')    
print(f'O dobro de {num} é igual a {numeros.dobro(num)}')
print(f'O triplo de {num} é igual a {numeros.triplo(num)}')
