# W pliku dane.txt znajduje się 200 wierszy (sprawdź katalog). Każdy wiersz zawiera 320 liczb naturalnych z przedziału
# od 0 do 255, oddzielonych znakami pojedynczego odstępu (spacjami). Przedstawiają one jasności kolejnych pikseli
# czarno-białego obrazu o wymiarach 320 na 200 pikseli (od 0 – czarny do 255 – biały). Napisz program(y), który(e) da(dzą)
# odpowiedzi do poniższych zadań. Odpowiedzi zapisz w pliku wyniki6.txt, a każdą odpowiedź poprzedź
# numerem oznaczającym odpowiednie zadanie.
#
# 10.1
# Podaj jasność najjaśniejszego i jasność najciemniejszego piksela.
# 10.2
# Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś symetrii.
# Obraz ma pionową oś symetrii, jeśli w każdym wierszu i-ty piksel od lewej strony przyjmuje tę samą wartość,
# co i-ty piksel od prawej strony, dla dowolnego 1 ≤ i ≤ 320.
# 10.3
# Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej kolumnie.
# Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się o więcej niż 128.
# Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden kontrastujący z nim sąsiedni piksel.
# 10.4
# Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie obrazka),
# złożonej z pikseli tej samej jasności.


the_brightness = float("-inf")
the_darkness = float("inf")

with open('pliki10_data.txt', 'r') as file:
    for line in file:
        nums = eval(line.replace(" ", ","))

        the_largest_number = max(nums)
        the_smallest_number = min(nums)

        if the_brightness < the_largest_number:
            the_brightness = the_largest_number

        if the_darkness > the_smallest_number:
            the_darkness = the_smallest_number

    print(f'jasność najjaśniejszego pixela to {the_brightness} a najciemniejszego to {the_darkness}')

# list_of_strings = []
# numbers = []
#
# with open('pliki10_data.txt', 'r') as file:
#     def returning_numbers():
#         text = file.readlines()
#         for line in text:
#             line = line.replace('\n', '')
#             list_ = line.split(' ')
#             list_of_strings.extend(list_)
#
#         for part in list_of_strings:
#             numbers.append(int(part))
#
#         return numbers
#
#
#     returning_numbers()
#     print(f'jasność najjaśniejszego pixela to {max(numbers)} a najciemniejszego to {min(numbers)}')