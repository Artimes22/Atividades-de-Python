'''tempo = int(input("Qantos anos seu carro tem? "))
if tempo <= 3:
    print("Seu carro esta novo")
else:
    print("Seu carro esta bem usado")
print("--FIM--")

nome = str(input("Qual seu nome: ")).strip().capitalize()
if nome == 'Artimes':
    print("Que nome maravilho")
print("Bom dia {}!".format(nome)) '''

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2
print("Sua media é {:.1f}".format(m))
if m >= 7:
    print("Aprovado")
else:
    print("Reprovado")    