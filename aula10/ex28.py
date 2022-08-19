import random
import time

print("vou pensar em um numero entre 1 e 5 e voce vai tentar adivinhar")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
numero = int(input("em qual numero eu estou pensando? "))
print("PROCESSANDO ...")
time.sleep(3)
maquina = random.randint(0,5)
if numero == maquina:
    print("PARABENS você acertou o número que eu pensei")
else:
    print("GANHEI, eu pensei no número {} e não no número {}".format(maquina, numero))
    
print(maquina)