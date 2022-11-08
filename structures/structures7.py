number = int(input("podaj liczbę której wartość bezwględną chcesz poznać: "))
new_number = 0

if number >= 0:
    print("wartość bezwględna twojej liczby to", number)
elif number < 0:
    new_number = number * -1
    print("wartość bezwględna twojej liczby to", new_number)