# Stwórz następującą strukturę danych (słownik):
# zamowienia = {"Klient_1335" : {"nazwa_potrawy" : "rosół", "ocena" : 5, "rachunek" : 20.0},
#               "Klient_222" {"nazwa_deseru” : "lody waniliowe", "rachunek" : 5.0 }}
# Następnie wyświetl nazwy wszystkich klientów i dla każdego z nich stwórz podsumowanie zamówienia:

zamowienia = {"Klient_1335": {"nazwa_potrawy": "rosół", "ocena": 5, "rachunek": 20.0},
              "Klient_222": {"nazwa_potrawy": "lody waniliowe", "rachunek": 5.0}}

for key in zamowienia:
    print(zamowienia['Klient_1335'])

    #TODO dokończyć