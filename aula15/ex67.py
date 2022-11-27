'''
n = int(input('Digite um número para saber a tabuada: '))
while True:
    
    print(f'''
# {n}X1 = {n * 1}
# {n}X2 = {n * 2}
# {n}X3 = {n * 3}
# {n}X4 = {n * 4}
# {n}X5 = {n * 5}
# {n}X6 = {n * 6}
# {n}X7 = {n * 7}
# {n}X8 = {n * 8}
# {n}X9 = {n * 9}
# {n}X10 = {n * 10}
''')
    n = int(input('Informe outro nùmero para saber a tabuada: '))
    if n == -1:
        break
print('Acabou')    
'''
while True:
    n = int(input('De qual número você quer ver a tabuada: '))
    if n < 0:
        break
    print('-'*30)
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)

print('PROGRAMA TABUADA ENCERRADO!')    

