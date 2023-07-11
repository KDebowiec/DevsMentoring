# Stwórz funkcję sprawdzającą, czy liczba jest pierwsza. Otestuj ją,
# pamiętając równocześnie o otestowaniu każdego edge-case’a (np. 1 nie jest liczbą pierwszą).
# Spróbuj stworzone testy umieścić w klasie.
#
# Uwaga:
# Aby uruchomić testy znajdujące się w klasie, np. TestIsPrime, użyj polecenia:
#
# >>> pytest tests/tests.py::TestIsPrime
def is_prime(number):
    dividers = 0
    for i in range(1, number+1):
        if number % i == 0:
            dividers += 1
    if dividers == 2:
        return True

