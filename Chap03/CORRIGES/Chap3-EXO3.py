n=(int(input("Saisir le chiffre de quilles tomber au première essaie")))
if n==10:
    print("STRIKE")

else:
    d=(int(input("Saisir le chiffre de quilles tomber au deuxième essai")))

    if n+d==10:
        print("spare")
    elif n+d>10 :
        print('valeur impossible')
    else :
        print('Score : ', n+d)
