# Utwórz zbiór składający się z 15 losowo wygenerowanych wartości typu int z przedziału 5 - 120.
# Następnie usuń ze zbioru wszystkie liczby parzyste.
import random
random_list = []
random_set = set(random_list)
elements_to_remove = []
element_set = set(elements_to_remove)
final_set = {}

for i in range(15):
    random_set.add(random.randint(5, 120))

for i in random_set:
    if i % 2 == 0:
        element_set.add(i)

final_set = random_set - element_set

print(final_set)

