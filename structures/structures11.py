for i in range(6):
    for j in range(7):
        print('*', end=' ')
    print()

print('następna figura')

number = 1
while number <= 9:
    print(('*' * number).center(9))
    number +=2