# Napisz program, który poprosi użytkownika o podanie imion kilku swoich dobrych znajomych.
# Korzystając z wprowadzonych danych, dla każdego z podanych znajomych, program ma wyświetlić
# spersonalizowany komunikat, na przykład powitanie, pozdrowienie, który będzie skierowany do konkretnej osoby.
person = None
person_list = []

while person != "q":
    print("Wpisz 'q' by zakonczyc.")
    person = input('podaj imie znajomego: ')
    if person != "q":
        person_list.append(person)
    for name in person_list:
        print(f'hej {name} co u Ciebie ')