from validacao import valor

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um número inteiro valido.') 
            continue
        else:
            return n 
    
    
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um número real valido.')
            continue
        else:
            return n        

 
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O número digitado foi {inteiro}')
print(f'O número digitado foi {real}')




