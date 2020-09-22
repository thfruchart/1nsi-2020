n = int(input('Entrer n :'))

for a in range(1, n+1 ) :
    reste =  n % a
    if reste == 0 :
        print(a)


