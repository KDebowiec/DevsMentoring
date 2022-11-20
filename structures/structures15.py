# Stwórz słownik przechowujący 5 dowolnych nr PESEL jako klucze i do każdego z nich przypisz cechy osób o podanym PESELu
# w formie kolejnego słownika (cechy te to: kolor_oczu, imie, nazwisko, wiek), czyli możliwa by była operacja:
#
# Za pomocą pętli for dodaj do każdej wartości w słowniku (która jest kolejnym słownikiem) nowy klucz (imię_matki)
# oraz nadaj odpowiednie wartości
#
# Usuń z słownika osoby, których pesel kończy się na znak ‘1’.
# Wydrukuj zawartość słownika w przyjaznej formie (w komunikacie mają nie wyświetlać się klamry {})



nr_pesel ={
'49385720512' : {'kolor_oczu': 'niebieski', 'imie' : 'Karol', 'Nazwisko' : 'Dureń', 'wiek' : '28'},
'56789024861' : {'kolor_oczu': 'niebieski', 'imie' : 'Stefan', 'Nazwisko' : 'Dudek', 'wiek' : '67'},
'56012348571': {'kolor_oczu': 'zielony', 'imie' : 'Jolanta', 'Nazwisko' : 'Kowalska', 'wiek' : '90'},
'58697857463': {'kolor_oczu': 'brązowy', 'imie' : 'Bożena', 'Nazwisko' : 'Bemben', 'wiek' : '12'},
'56781234567': {'kolor_oczu': 'brązowy', 'imie' : 'Krystyna', 'Nazwisko' : 'Grdyk', 'wiek' : '45'}}

for key in nr_pesel:
    nr_pesel['49385720512']["imie_matki"] = 'Adelajda'
    nr_pesel['56789024861']["imie_matki"] = 'Brygida'
    nr_pesel['56012348571']["imie_matki"] = 'Samanta'
    nr_pesel['58697857463']["imie_matki"] = 'Beata'
    nr_pesel['49385720512']["imie_matki"] = 'Wiola'
    nr_pesel['56781234567']["imie_matki"] = 'Zuzanna'

for key in list(nr_pesel):
    if key[10] == '1':
        del nr_pesel[key]

list = list(nr_pesel.keys())
for key in list:
    print(key, nr_pesel[key])
