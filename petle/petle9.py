start_fuel_input = int(input('początkowy poziom paliwa: '))
start_fuel = 0
astronauts_input = int(input('początkowa liczba astronautów: '))
astronauts = 0
reach=0
current_level = 0
usage = 0
interval = 0
x=100

if start_fuel_input <= 30000 and start_fuel_input >= 5000:
    start_fuel = start_fuel_input
else:
    print('podaj poziom paliwa z zakresu 5000-30000')
    
if astronauts_input <= 7 and astronauts_input > 0:
    astronauts = astronauts_input
else:
    print('podaj liczbę astronautów 0-7')
    
reach= int((start_fuel /(300 + 100 * astronauts))*100)
usage = 300 + 100*astronauts
interval = start_fuel / usage

for i in range(reach,0,-100):
    
    print(f'przebyto {x}  km')
    x+=100

if x >= 2000:
    print('statek dotarł do orbity')
else:
    print('statek nie dotarł do orbity')