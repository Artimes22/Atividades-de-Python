d = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos Km foram andados com o carro? "))
pago = (d * 60) + (km * 0.15)
print("O total a pagar pelo aluguel do carro é R$ {:.2f}" .format(pago))