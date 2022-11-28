# Utwórz zbiór składający się z 15 losowo wygenerowanych wartości typu int z przedziału 5 - 120.
# Następnie usuń ze zbioru wszystkie liczby parzyste.
import random
random_list = []
elements_to_remove = []
final_set = {}

for i in range(15):
    random_list.append(random.randint(5, 120))

random_set = set(random_list)
for i in random_set:
    if i % 2 == 0:
        elements_to_remove.append(i)
remove_set = set(elements_to_remove)
final_set = random_set - remove_set

print(final_set)

