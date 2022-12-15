# Napisz funkcję, ktora przyjmować będzie godzinę i minutę (wykorzystaj keyword arguments) i powinna ona zwrócić
# kąt (podany w stopniach) między wskazówką godzinową a minutową w tym podanym czasie.
#
# Podpowiedź:
# Możesz wykorzystać funkcję abs w celu obliczania wartości bezwzględnej, np.
# print(abs(-5)) # 5
# def one_list(**kwargs):
def equation(**kwargs):
    angle = abs(6 * kwargs['minutes_on_clock'] - 30 * (kwargs['hours_on_clock'] + kwargs['minutes_on_clock'] / 60))
    if angle > 180:
        ultimate_angle = 360 - angle
        print(f'kąt między wskazówkami to {ultimate_angle}')
    else:
        print(f'kąt między wskazówkami to {angle}')


time = input('która jest godzina? podaj w formacie 12:00: ')
time_list = time.split(':')
hour = int(time_list[0])
minute = int(time_list[1])
equation(hours_on_clock=hour, minutes_on_clock=minute)



