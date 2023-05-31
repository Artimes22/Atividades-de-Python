import moeda

valor = float(input('Informe o preço do produto: R$ '))

print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade)}')
print(f'Pagando no credito o valor de {moeda.moeda(valor)}fica 10% a mias no valor e o produto custara {moeda.moeda(moeda.dez)}')
print(f'Pagando avista você ganha 15% de desconto e o valor de {moeda.moeda(valor)} vai ficar {moeda.moeda(moeda.desconto)}')