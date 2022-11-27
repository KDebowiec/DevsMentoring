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
new_city = None
new_amount = None

while True:
    new_data = input('podaj miasto i opad np. Boston 12, by zobaczyć wynik dodaj puste: ')
    if new_data != '':
        new_data = new_data.split()
        new_city = new_data[0]
        new_amount = new_data[1]
        city_rain_dict.update({new_city: new_amount})
    else:
        print(city_rain_dict)
