def echange(t,i,j):
    aux = t[i]
    t[i] = t[j]
    t[j] = aux
    return t
# brouillon
t = [10,20,30,40,50] # len(t) = 5
echange(t, 0, 4)
echange(t, 1, 3)
# brouillon 2
t = [10,20,30,40,50,60,70,80] # len(t) = 8
echange(t, 0, 7)
echange(t, 1, 6)
echange(t, 2, 5)
echange(t, 3, 4)
# brouillon 3
t = [10,20,30,40,50,60,70,80] # len(t) = 8
x = 0
y = 7
for i in range( len(t)//2 ):
    echange(t,  x ,   y  )
    x += 1
    y -= 1

# brouillon 4
t = [10,20,30,40,50,60,70,80,90] # len(t) = 9
x = 0
y = len(t)-1
for i in range( len(t)//2 ):
    echange(t,  x ,   y  )
    x += 1
    y -= 1

# solution
def miroir(t):
    x = 0
    y = len(t)-1
    for i in range( len(t)//2 ):
        echange(t,  x , y  )
        x += 1
        y -= 1
    return t

# solution "élégante"
def miroir(t):
    for i in range( len(t)//2 ):
        echange(t,  i , len(t)-1-i )
    return t


print("miroir([1,2,3,4,5])=", miroir([1,2,3,4,5]))
print("miroir([1,2,3,4,5,6])=", miroir([1,2,3,4,5,6]))
print("miroir([])=", miroir([]))
