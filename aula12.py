nome = str(input("Qual o seu nome: ")).upper()
if nome == "ARTIMES" :
    print("Que nome bonito!")
elif nome == "PEDRO" or nome == "MARIA" or nome == "JOSÉ":
    print("Seu nome é bem popular no Brasil")
else:
    print("Seu nome é bem comum")    
print("Tenha um bom dia, {}!".format(nome))