firstSide = int(input('podaj długość pierwszego boku: '))
secondSide = int(input('podaj długość drugiego boku: '))
thirdSide = int(input('podaj długość trzeciego boku: '))

if firstSide * firstSide + secondSide * secondSide == thirdSide * thirdSide:
    print('to jest trójkąt prostokątny') 
else:
    print('to nie jest trójkąt prostokątny')