n = int(input('Entrer n :'))
compteur = 0

for a in range(1, n+1 ) :
    reste =  n % a
    if reste == 0 :
        #print(a)
        compteur = compteur + 1

if compteur == 2:
    print(n , 'est premier')
else :
    print(n , ' NON premier')


