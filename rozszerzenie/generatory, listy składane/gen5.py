# Mając tak utworzoną listę liczb:
# numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]
# Wykorzystując, list comprehension, utwórz nową o nazwie filtered_numbers, w której znajdą się tylko liczby niedodatnie z numbers.
numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]

filtered_numbers = [i for i in numbers if i < 0]
print(filtered_numbers)
