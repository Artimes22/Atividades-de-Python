import moeda

valor = float(input('Informe o preço do produto: R$ '))
metade = moeda.metade(valor)
dobro = moeda.dobro(valor)
dez = moeda.dez(valor)
desconto = moeda.desconto(valor)
print(f'O dobro do valor do produto é R${dobro:.2f}')
print(f'A metade do valor do protudo é R${metade:.2f}')
print(f'Pagando no credito fica 10% a mias no valor e o produto custara {dez:.2f}')
print(f'Pagando avista você ganha 15% de desconto e fica R${desconto:.2f}')