# Stwórz program, który zwróci kwadraty oraz sześciany wartości zapisanych w liście. Wykorzystaj funkcje lambda.

oryginal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x**2, oryginal))

cube = list(map(lambda x: x**3, oryginal))
