dis = float(input("Qual a distancia da viagem? "))
print("Você vai começar uma viagem de {:.1f}Km".format(dis))
if dis <= 200:
    total = dis * 0.50
else:
    total = dis * 0.45
print("O preço da passagem vai ser de {:.2f}".format(total))    