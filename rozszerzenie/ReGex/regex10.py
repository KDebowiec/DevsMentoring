# Efektem zbierania pomiarów temperatury okazał być się plik tekstowy, który zawiera datę pomiaru oraz wartość.
# W jaki sposób możliwe jest wydzielenie tylko dat w takiej sytuacji?
# Poniżej znajduje się fragment przykładowych danych wejściowych.
#
# "2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"
import re


text = "2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"
match = re.findall("[0-9]+[-/.][0-9a-z]+[-/.][0-9]+", text)
print(match)