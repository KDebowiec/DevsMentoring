#Napisz program, który poprosi użytkownika o podanie dwóch liczb całkowitych i obliczy ich iloraz.
#Jeśli druga liczba jest równa zero, program powinien wygenerować wyjątek ZeroDivisionError i wyświetlić odpowiedni komunikat.
#Program powinien również zawierać blok finally, który zawsze wyświetla komunikat "Dziękuję za skorzystanie z programu".
try:
    x = int(input('podaj pierwsza'))
    y = int(input('podaj drugą'))
    solution = x / y
    print(f'wynik to {solution}')
except ZeroDivisionError:
    print('Nie dziel przez zero chuju')
finally:
    print('Dziękuje za skorzystanie z programu')