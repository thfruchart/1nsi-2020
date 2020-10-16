def echange(t,i,j):
    aux = t[i]
    t[i] = t[j]
    t[j] = aux
    return t

print(echange([10,20,30,40], 1,2))