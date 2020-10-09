# Exercice 1 question1)
from random import randint
valeur_maxi = 1
valeur_mini = 1000
t = [0]*10

for i in range(len(t)):
    v = randint(1,1000)
    t[i] = v
    if v > valeur_maxi:
        valeur_maxi = v
    if v < valeur_mini:
        valeur_mini = v


print(t)
print(valeur_maxi)
print(valeur_mini)

