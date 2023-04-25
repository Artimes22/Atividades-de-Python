numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n= int(input('Informe um numero entre (0 e 20): '))
    if 0<= n <=20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numero[n]}')
