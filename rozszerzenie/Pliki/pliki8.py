# Stwórz funkcję, która przyjmować będzie dowolny zestaw parametrów reprezentowanych przez **kwargs.
# Następnie niech taka funkcja utworzy z kwargs słownik, który będzie składał się z takim samych par
# klucz:wartość co kwargs, ale będą one odwrócone.
# Na przykład:
# Gdy kwargs przyjmie postać {klucz1:wartość1, klucz2:wartość2}, to powstały słownik ma mieć następującą
# strukturę: {wartość1:klucz1, wartość2:klucz2}.
#
# Następnie zapisz tak utworzony słownik do pliku o nazwie output.json.
def match(**kwargs):
    new_dict = {}
    list_of_values = [kwargs.get("imie_zawodnika"), kwargs.get("kraj_pochodzenia")]
    list_of_keys = list(kwargs.keys())
    for element in list_of_values:
        for i in list_of_values:
            list_of_values[element] = new_dict[i]


#TODO co ja w ogole kurwa robie

def main():
    fighter_name = input('podaj nazwisko zawodnika: ')
    fighter_country = input('podaj kraj pochodzenia zawodnika: ')

    match(imie_zawodnika=fighter_name, kraj_pochodzenia=fighter_country)


if __name__ == '__main__':
    main()
