n = int(input('entrer une année n : '))

if n%400 == 0:
    print ("L'année", n, 'est bissextile')
elif n%100 == 0:
    print ("L'année", n, "n'est pas bissextile")
elif n%4 == 0:
    print ("L'année", n, 'est bissextile')
else :
    print ("L'année", n, "n'est pas bissextile")

