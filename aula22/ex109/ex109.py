import moeda

valor = float(input('Informe o preço do produto: R$ '))

print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)} é R${moeda.metade(valor, True)}')
print(f'Pagando no credito fica 10% a mais no valor e o produto custara {moeda.dez(valor, True)}')
print(f'Pagando avista você ganha 15% de desconto e fica R${moeda.desconto(valor, True)}')