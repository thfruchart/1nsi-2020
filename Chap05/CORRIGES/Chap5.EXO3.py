# Exercice 3
def somme(tab):
    s = 0
    for i in range(len(tab)):
        s = s + tab[i]
    return s

def moyenne(t):
    return somme(t) / len(t)

print(somme([10,20,30,40,50]))
print(moyenne([10,20,30,40,50]))

