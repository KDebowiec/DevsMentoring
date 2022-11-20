# Napisz program, który poprosi użytkownika o podanie imion kilku swoich dobrych znajomych.
# Korzystając z wprowadzonych danych, dla każdego z podanych znajomych, program ma wyświetlić
# spersonalizowany komunikat, na przykład powitanie, pozdrowienie, który będzie skierowany do konkretnej osoby.
person = None
person_list = []

person = input('podaj imiona swoich znajomych: ')

person_list = person.split()

print(f'hej {person_list[0]} co u Ciebie ')
#TODO itp itd coś chyba polecienie nieteges bo po co tu lista w ogóle