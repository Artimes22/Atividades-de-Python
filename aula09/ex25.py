from unicodedata import name


nome = str(input("Qual o seu nome? ")).strip()
print("Tem Silva no seu nome: {}" .format('SILVA' in nome.upper))