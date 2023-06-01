def metade(preço=0, formato = False ):
    metade =  preço / 2
    return metade if formato is False else moeda(metade)

def dobro(preço=0, formato = False):
    dobro = preço * 2
    return dobro if formato is False else moeda(dobro)
    
def dez(preço=0, formato = False):
    dez = preço + (preço * 10 / 100)
    return dez if not formato else moeda(dez)

def desconto(preço=0, formato = False):
    des = preço - (preço * 15 / 100)
    return des if not formato else moeda(des)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

