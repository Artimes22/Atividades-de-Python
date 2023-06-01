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

def resumo(preço=0, taxaa=10, taxar=15):
    print('-'*30)
    print(' RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado \t{moeda(preço)}')
    print(f'Dobro do preço \t\t{dobro(preço, True)}')
    print(f'Metade do preço \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento \t{dez(preço, True)}')
    print(f'Com {taxar}% de desconto \t{desconto(preço, True)}')
    print('-'*30)