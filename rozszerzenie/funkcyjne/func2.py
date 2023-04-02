# Napisz program, który posortuje listę krotek przy wykorzystaniu funkcji lambda oraz metody .sort().
# Lambdę wykorzystuj przy wskazaniu, według którego (drugiego) elementu ma odbywać się sortowanie.
#
to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorting = to_sort.sort(key=lambda x: x[1])
print(sorting)