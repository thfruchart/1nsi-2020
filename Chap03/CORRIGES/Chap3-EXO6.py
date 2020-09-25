from turtle import *

n = int (input('Entrer un entier n : '))
c = 20

for ligne in range(n) :
    for colonne in range(n):
        up()
        goto(ligne * c, colonne *c)
        if (ligne+colonne)%2 == 0:
            # on dessine un carré noir
            down()
            begin_fill()
            for _ in range(4):
                forward(c)
                left(90)
            end_fill()
        else :
            #on dessine un carré blanc
            down()
            for _ in range(4):
                forward(c)
                left(90)



