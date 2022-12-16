# Wyobraź sobie, że jesteś pogodynką i robisz zestawienie opadów deszczu na dany miesiąc. Problem polega jednak na tym,
# że dane miasta wraz z opadami są nieuporządkowane oraz użytkownik może wpisywać nieskończenie wiele par:
# miasto oraz opad aż do momentu podania pustej linii. Twoim zadaniem jest zinterpretowanie podanych danych wejściowych
# i podać wynik na wzór poniższego przykładu.
# Wejście:
# Boston 12
# Londyn 10
# Boston 12
# [pusta linia]
#
# Wyjście:
# Boston : 24
# Londyn : 10
city_rain_dict = {}

while True:
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



