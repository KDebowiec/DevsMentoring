# Przekształć poniższy tekst, dopisując w nawiasach do polskich nazw ptaków ich łacińskie odpowiedniki.
#
# Skorzystaj w tym celu ze słownika zawierającego następujące elementy:
# {'kos' : 'Turdus merula', 'wilga' : 'Oriolus oriolus', 'rudzik' : 'Erithacus rubecula',
#  'kukulka' : 'Cuculus canorus', 'pleszka' : 'Phoenicurus phoenicurus', 'bogatka' : 'Parus major',
#  'drozd' : 'Turdus philomelos', 'zieba' : 'Fringilla coelebs', 'dzwoniec' : 'Chloris chloris',


dictionary_birds = {'kos': 'Turdus merula', 'wilga': 'Oriolus oriolus', 'rudzik': 'Erithacus rubecula',
                    'kukulka': 'Cuculus canorus', 'pleszka': 'Phoenicurus phoenicurus', 'bogatka': 'Parus major',
                    'drozd': 'Turdus philomelos', 'zieba': 'Fringilla coelebs', 'dzwoniec': 'Chloris chloris',
                    'szczygiel': 'Carduelis carduelis', 'szpak': 'Sturnus vulgaris',
                    'kopciuszek': 'Phoenicurus ochruros'}

text = 'W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile' \
       ' pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka.' \
       ' Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. ' \
       'Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew.' \
       ' Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. ' \
       'Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel.'

for bird in dictionary_birds.keys():
    text = text.replace(bird, f"{bird}({dictionary_birds[bird]})")

print(text)
