'''import math

n = int(input('De qual número você quer o fatorial? '))
f = math.factorial(n)
print('O fatorial de {} é {} ' .format(n, f))
'''

n = int(input('De qual número você quer o fatorial? '))
c = n
f = 1
print('Calculando o {}! = ' .format(n), end='')
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c 
    c -= 1
print('{} '.format(f))    
