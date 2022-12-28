# W załączeniu znajduje się plik data.json. Przechowuje on informacje o różnych pakietach informacji. Twoim zadaniem jest
# napisanie skryptu, który będzie odczytywał taki pliku i drukował poniższy komunikat
# zawierający informacje o każdym z pakietów:
import json

jsondata = open('10 Podstawy Szkolenie 8 - data.json').read()

json_object = json.loads(jsondata)

print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
imdata = json_object["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        # print fields formatted in columns
        print("{0:50} {1:20} {2:7} {3:6}".format(dn, descr, speed, mtu))
#TODO do obgadania w chuj bo nic tu nie rozumiem, rozwiązanie z neta