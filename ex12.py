valor = float(input('Qual o valor do produto? '))
novo = valor - (valor*5/100)
print('O produto de valor R${:.2f}, preço com 5% de desconto é R${:.2f}'.format(valor, novo))