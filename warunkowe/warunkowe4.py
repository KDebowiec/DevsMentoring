# print('zagrajmy w grę kamień, papier, nożyce!')
# firstPlayer = input('figura pierwszego gracza: ')
# secondPlayer = input('figura drugiego gracza: ')
#
# if firstPlayer == 'papier' and secondPlayer == 'kamień':
#     print('wygrał pierwszy gracz!')
# elif firstPlayer == 'kamień' and secondPlayer == 'papier':
#     print('wygrał drugi gracz!')
# elif firstPlayer == 'nożyce' and secondPlayer == 'papier':
#     print('wygrał pierwszy gracz!')
# elif firstPlayer == 'papier' and secondPlayer == 'nożyce':
#     print('wygrał drugi gracz!')
# elif firstPlayer == 'kamień' and secondPlayer == 'nożyce':
#     print('wygrał pierwszy gracz!')
# elif firstPlayer == 'nożyce' and secondPlayer == 'kamień':
#     print('wygrał drugi gracz!')
# elif firstPlayer == secondPlayer:
#     print('jest remis!')



question = "Podaj swoją figurę(kamień/papier/nożyce): "

k = "kamień"
p = "papier"
n = "nożyce"


win_prompt = "{} wygrywa!"
tie_prompt = "Remis!"
invalid_prompt = "Nie ma takiej figury!"

player_1 = "Gracz 1"
first = input(question)

player_2 = "Gracz 2"
second = input(question)

if first == k:
    if second == p:
        print(win_prompt.format(player_2))
    elif second == n:
        print(win_prompt.format(player_1))

elif first == p:
    if second == n:
        print(win_prompt.format(player_2))
    elif second == k:
        print(win_prompt.format(player_1))

elif first == n:
    if second == k:
        print(win_prompt.format(player_2))
    elif second == p:
        print(win_prompt.format(player_1))

elif first == second:
    print(tie_prompt)

else:
    print(invalid_prompt)