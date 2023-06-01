def metade(preço=0):
    metade =  preço / 2
    return metade

def dobro(preço=0):
    dobro = preço * 2
    return dobro
    
def dez(preço=0):
    dez = preço + (preço * 10 / 100)
    return dez

def desconto(preço=0):
    des = preço - (preço * 15 / 100)
    return des

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

