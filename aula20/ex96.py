def area(larg, compr):
    a = larg * compr
    print(f'A área de um um terreno {larg:.2f} x {compr:.2f} é igual a {a:.2f}m²')
    
print('   ----CONTROLE DE TERRENOS----')    
print('-'*30)
largura = float(input('Qual a largura do terreno? '))
comprimento = float(input('Qual o comprimento do terrno? '))
area(largura, comprimento) 
