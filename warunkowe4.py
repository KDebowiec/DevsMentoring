print('zagrajmy w grę kamień, papier, nożyce!')
firstPlayer = input('figura pierwszego gracza: ')
secondPlayer = input('figura drugiego gracza: ')

if firstPlayer == 'papier' and secondPlayer == 'kamień':
    print('wygrał pierwszy gracz!')
elif firstPlayer == 'kamień' and secondPlayer == 'papier':
    print('wygrał drugi gracz!')
elif firstPlayer == 'nożyce' and secondPlayer == 'papier':
    print('wygrał pierwszy gracz!')
elif firstPlayer == 'papier' and secondPlayer == 'nożyce':
    print('wygrał drugi gracz!')
elif firstPlayer == 'kamień' and secondPlayer == 'nożyce':
    print('wygrał pierwszy gracz!')
elif firstPlayer == 'nożyce' and secondPlayer == 'kamień':
    print('wygrał drugi gracz!')
elif firstPlayer == secondPlayer:
    print('jest remis!')
#todo: zabezpieczenie przed wyborem innym niż papier kamień lub nożyce