firstSide = int(input('podaj długość pierwszego boku: '))
secondSide = int(input('podaj długość drugiego boku: '))
thirdSide = int(input('podaj długość trzeciego boku: '))

right_triangle = firstSide**2 + secondSide**2 == thirdSide**2

if right_triangle:
    print('to jest trójkąt prostokątny') 
else:
    print('to nie jest trójkąt prostokątny')