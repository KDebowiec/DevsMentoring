# Zadanie Ciphering
#
# Stworzyć mini-projekt w oparciu o fasadę, który dostarczać będzie następujące funkcjonalności:
#
# 1. Encrypt plain text (ROT47/ROT13)
# 2. Save encrypted texts to file
# 3. Decrypt encrypted text from file (ROT47/ROT13)
# 4. Print encrypted words stored in memory
# 5. Exit


# muszą być stworzone klasy ROT47 i ROT13 oraz klasa ROT, po której dziedziczą,
# klasa menu,
# klasa FileHandler, która obsługuje zapisywanie do pliku i odczytywanie z pliku
# klasa pomocnicza InputReader, która rzuca wyjątkami jak ktoś wpisze np ą,ę,ó
# kod opisany za pomocą dock stringów
# zastosuj zasadę test driven development
# input przechowany w atrybucie


class ROT:
    def __init__(self, text, result):
        self.text = ''
        self.result = ''


class FileHandler:
    def __init__(self, result):
        self.result = result
        self.saving_to_file()

    def saving_to_file(self):
        file = open('coded.txt', 'x')
        file.write(self.result)
        file.close()


class ROT47(ROT, FileHandler):
    def __init__(self, text, result):
        super().__init__(text, result)
        self.encoding_to_rot47(text)

    def encoding_to_rot47(self, text):
        result = ''
        for char in text:
            if 33 <= ord(char) <= 126:
                new_char = chr((ord(char) - 33 + 47) % 94 + 33)
            else:
                new_char = char
            result += new_char
        print(result)
        saving = int(input('Do You want to save it to file? type 1, if not, type 2'))
        if saving == 1:
            super().saving_to_file()
        else:
            pass


class ROT13(ROT, FileHandler):
    def __init__(self, text, result):
        super().__init__(text, result)
        self.encoding_to_rot13(text)

    def encoding_to_rot13(self, text):
        result = ''
        for char in text:
            if char.isalpha():
                if char.islower():
                    new_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
                else:
                    new_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                new_char = char
            result += new_char
        print(result)
        saving = int(input('Do You want to save it to file? type 1, if not, type 2'))
        if saving == 1:
            super().saving_to_file()
        else:
            pass
class Menu(ROT13, ROT47):
    def __init__(self, text, result):
        super().__init__(text, result)
        self.menu()

    def taking_text_to_encode(self):
        """
        Function takes text which user wants to code
        """
        self.text = input('type in text to code: ')
        return self.text


    def menu(self):
        print('Welcome, Do you want to encode you text in ROT13 or ROT47?')
        choice = int(input('type 1 if ROT13, type 2 if ROT47'))
        if choice == 1:
            self.taking_text_to_encode()
            ROT13.encoding_to_rot13(self.text)

object = Menu(text = '', result='')
object.menu()
