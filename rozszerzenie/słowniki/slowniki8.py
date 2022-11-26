# Napisz program, który wydrukuje wszystkie unikalne wartości ze słownika.
# Dla danych:
# { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
# Oczekujemy wyniku:
# “S002”, “S009”, “S007”
random = {"V": "S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX": "S005", "X": "S009", "XI": "S007"}
unique_values = []

random_values = list(random.values())

for i in random_values:
    if random_values.count(i) == 1:
        unique_values.append(i)

print(' '.join(unique_values))