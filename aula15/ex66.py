n = c = s = 0
while True:
    n = int(input('Digite um número [digite 999 para parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números e a soma entre eles é de {s}') 
print('Acabou')   
