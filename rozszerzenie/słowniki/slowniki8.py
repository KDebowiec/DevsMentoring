# Napisz program, który wydrukuje wszystkie unikalne wartości ze słownika.
# Dla danych:
# { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
# Oczekujemy wyniku:
# “S002”, “S009”, “S007”
random = {"V": "S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX": "S005", "X": "S009", "XI": "S007"}
random_values = []
unique_values = None

random_values = random.values()
print(random_values)

unique_values = set(random_values)
print(unique_values)

#TODO dokonczyc