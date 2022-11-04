k = int(input('podzielne przez jaką liczbę mają być wyświetlane liczby?: '))
l = int(input('dolna granica przedziału z jakiego mają być wyświetlane liczby?: '))
m = int(input('górna granica przedziału z jakiego mają być wyświetlane liczby?: '))




for i in range(l,m):
    if i % k == 0:
        print(i)
    else:
        continue