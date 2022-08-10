n = float(input('Qual o valor que você tem em sua carteira? R$'))
dolar = n / 5.35
euro = n / 5.41
arge = n / 0.041
print('Com R${:.2f} você pode comprar {:.2f} dolars'.format(n, dolar))
print('Com R${:.2f} você pode comprar {:.2f} euros'.format(n, euro))
print('Com R${:.2f} você pode comprar {:.2f} pesos argentino'.format(n, arge))