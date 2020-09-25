n = int (input('Entrer un entier n : '))
for i in range(1, n+1):
    if i%15==0:
        print("fizzbuzz")
    elif i%3 == 0:
        print('fizz')
    elif i%5 == 0 :
        print('buzz')
    else :
        print(i)


