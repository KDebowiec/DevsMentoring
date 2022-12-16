city_rain_dict = {}
new_data = input('podaj miasto i opad np. Boston 12, by zobaczyć wynik dodaj puste: ')

while new_data:
    new_data = input('podaj miasto i opad np. Boston 12, by zobaczyć wynik dodaj puste: ')
    if new_data:
        new_data = new_data.split()
        new_city = new_data[0]
        new_amount = int(new_data[1])

        if new_city in city_rain_dict:
            new_amount = int(new_data[1]) + city_rain_dict.get(new_city)

        city_rain_dict.update({new_city: new_amount})
    elif new_data == 0:
        break
    else:
        for i in city_rain_dict:
            print(i, city_rain_dict[i])
        break
