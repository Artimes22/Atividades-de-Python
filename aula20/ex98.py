import time
def linha():
    print('-='*20)
    
def contador(i, f, p):
    if p < 0:
        p *= -1 
    if p == 0:
        p = 1  
    linha()    
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            time.sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            time.sleep(0.5)
            cont -= p        
    print('FIM')
    
contador(1, 10, 1)    
contador(20, 0, 2)
linha()
print('Agora é sua vez de criar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
linha()