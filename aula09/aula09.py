frase = "Curso em Video Python"
print(frase)
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(len(frase))
print(frase.count('o',0,13))
print(frase.find('deo'))
print('curso' in frase)
print('Curso' in frase)
print(frase.replace('Python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
frase3 = ['Curso','em','Video','Python']
print('-'.join(frase3))

print('')

print('-'*30)

print('')

frase2 = "   Aprenda Python  "
print(frase2)
print(len(frase2))
print(frase2.strip())
print(len(frase2.strip()))
print(frase2.lstrip())
print(frase2.rstrip())