# Exercice 3
def produit(tab):
    s = 1
    for i in range(len(tab)):
        s = s * tab[i]
    return s

def produit(tab): # amélioré
    s = 1
    for i in range(len(tab)):
        print('i=',i)
        if tab[i] == 0:
            return 0
        else :
            s = s * tab[i]
    return s


print(produit([10,0,30,40,50,60,70,80]))


