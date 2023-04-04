# Stwórz program, który przekonwertuje listę krotek na listę stringów. Wykorzystaj map().
#
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]


# ['red pink', 'white black', 'orange green']


nums = list(map(lambda x: ' '.join(x), colors))


print(nums)