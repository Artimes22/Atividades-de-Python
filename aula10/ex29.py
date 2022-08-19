vel = int(input("Qual a velocidade atual do carro? "))
multa = (vel - 80) * 7
if vel > 80:
    print("!!MULTADO!! \nVocê ultrapassou a velocidade limite e tem uma multa de R$ {:.2f}" .format(multa))
print("Tenha um Bom Dia! Dirija com cuidado")    

