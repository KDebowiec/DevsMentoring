# W stringu HTML, wszystkie elementy otoczone są pewnymi znacznikami HTML (<p>Twój tekst</p>, <h1>Twój tekst2</h1> itd.).
# Każdy znacznik ma następującą postać: <znacznik>Tekst</znacznik>.
#
# Twoje zadanie to określić, czy podany tekst jest prawidłowym elementem kodu HTML, czyli czy składa się z
# odpowiednio skonstruowanych znaczników wraz z dowolnym tekstem pomiędzy nimi. Trudność, jaką możesz tutaj napotkać,
# to konieczność ominięcia, tzw. chciwego przeszukiwania, które omówiliśmy w szkoleniu.
import re

txt = '<p>Learn about regular expressions here.</p> <p>You\'re going to love them!</p>'

finding = re.findall(r'<[a-z]+>.*?</[a-z]+>', txt)

print(finding)
# [\sa-zA-Z0-9\\_\\!\\.]+