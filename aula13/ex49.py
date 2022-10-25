num = int(input("Digite qual número você quer a taboada: "))
for i in range(0, 11):
    print('{} x  {:2} =  {}'.format(num, i ,(num*i)))