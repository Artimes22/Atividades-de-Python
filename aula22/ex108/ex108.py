import moeda

valor = float(input('Informe o preço do produto: R$ '))

print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é R${moeda.moeda(moeda.metade(valor))}')
print(f'Pagando no credito fica 10% a mais no valor e o produto custara {moeda.moeda(moeda.dez(valor))}')
print(f'Pagando avista você ganha 15% de desconto e fica R${moeda.moeda(moeda.desconto(valor))}')