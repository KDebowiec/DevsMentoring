# Stwórz funkcję, która przyjmować będzie dowolny zestaw parametrów reprezentowanych przez **kwargs.
# Następnie niech taka funkcja utworzy z kwargs słownik, który będzie składał się z takim samych par
# klucz:wartość co kwargs, ale będą one odwrócone.
# Na przykład:
# Gdy kwargs przyjmie postać {klucz1:wartość1, klucz2:wartość2}, to powstały słownik ma mieć następującą
# strukturę: {wartość1:klucz1, wartość2:klucz2}.
#
# Następnie zapisz tak utworzony słownik do pliku o nazwie output.json.
import json
def match(**kwargs):
    new_dict = {}
    for element in kwargs:
        new_dict[kwargs[element]] = element
    return new_dict


def saving_to_json(new_dict):
    with open('pliki8_data.json', 'w') as outfile:
        json.dump(new_dict, outfile)



fighter_name = input('podaj nazwisko zawodnika: ')
fighter_country = input('podaj kraj pochodzenia zawodnika: ')

match(imie_zawodnika=fighter_name, kraj_pochodzenia=fighter_country)
new_dict = match()
saving_to_json(new_dict)

