import random
bottom_number = int(input('podaj dolny przedział z jakiego ma zostać wylosowana liczba: '))
top_number = int(input('podaj gorny przedział z jakiego ma zostać wylosowana liczba: '))
number = random.randint(bottom_number,top_number)
user_guess = user_guess = int(input("zgadnij liczbę: "))
start_points= top_number - bottom_number
points = 0
print(number)

if user_guess == number:
    print('zgadłeś!')
    print('dostajesz', start_points, "punktów")
else:
    points = start_points -1
    while user_guess != number:
       user_guess = int(input("zgadnij liczbę: "))
       points = points - 1
    if user_guess == number:
        print('zgadłeś!')
        print('dostajesz', points, "punktów")