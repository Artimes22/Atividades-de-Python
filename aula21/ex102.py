#--------------------------------FATORIAL DE UM NÚMERO E CONTA---------------------------#

def fatorial(num = 1, show=False):
    """
        ->Calcula o fatorial de um número.
    PARA - n: o numero a ser calculado.
    PARA - show: (opcional) mostrar ou não a conta 
    return: O valor fatorial de n.     
    """
    f = 1
    for c in range (num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')    
        f *= c
        
    return f

n=(int(input('Digite um valor: ')))
print(fatorial(n, show=True))