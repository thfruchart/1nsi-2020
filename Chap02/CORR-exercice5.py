# correction de l'exercice 5
total = 0
n = int(input('Entrer n :'))
for i in range(1, n+1): # a prend les valeurs de 1 à n inclus (n+1 exclu)
    total = total+i    # x est un accumulateur des valeurs de a
print(' 1 + 2 +...+',n,' = ' , total )