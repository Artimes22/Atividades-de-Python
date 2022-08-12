import math
ang = float(input("Informe o ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print("O ângulo de {} tem SENO igual a {:.2f}".format(ang, sen))
print("O ângulo de {} tem COSENO igual a {:.2f}".format(ang, cos))
print("O ângulo de {} tem TANGENTE igual a {:.2f}".format(ang, tan))