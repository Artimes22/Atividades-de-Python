def lin():
    print('')
    print('-'*30)
    print('')
    
def soma(a, b):
    print(f' A = {a} e B = {b}')
    soma = a + b
    print(f' A soma dos dois valores é igual a {soma}')

soma(4, 9)
soma(5, 10)

lin()

def contador (*num):
    tam = len(num)
    print(f'Recebi {num} e tem {tam} valores')
    
contador(1, 2, 3)
contador(4, 5, 6, 7)
contador(8, 9, 1, 20, 2, 4, 8)    

lin()     

def dobra (lst):
    pos= 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1

valores=[2, 4, 5, 8]
dobra(valores)
print(valores)       

lin()

def soma1(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    
soma1(4, 8)
soma1(1, 2, 7)
soma1(4, 9, 2, 4, 3)         
