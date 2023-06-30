# Zadanie Ciphering
#
# Stworzyć mini-projekt w oparciu o fasadę, który dostarczać będzie następujące funkcjonalności:
#
# 1. Encrypt plain text (ROT47/ROT13)
# 2. Save encrypted texts to file
# 3. Decrypt encrypted text from file (ROT47/ROT13)
# 4. Print encrypted words stored in memory
# 5. Exit
#
#
# muszą być stworzone klasy ROT47 i ROT13 oraz klasa ROT, po której dziedziczą,
# klasa menu,
# klasa FileHandler, która obsługuje zapisywanie do pliku i odczytywanie z pliku
# klasa pomocnicza InputReader, która rzuca wyjątkami jak ktoś wpisze np ą,ę,ó
# kod opisany za pomocą dock stringów
# zastosuj zasadę test driven development
# input przechowany w atrybucie
import re
encrypted_tekst_to_save = ''
class ROT:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                encrypted_char = self.rotate_char(char)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        encrypted_tekst_to_save = encrypted_text
        return encrypted_text

    def decrypt(self, text):
        print(self.encrypt(text))
        return self.encrypt(text)


class ROT13(ROT):
    def __init__(self):
        super().__init__(13)

    def rotate_char(self, char):
        if char.islower():
            return chr((ord(char) - ord('a') + self.shift) % 26 + ord('a'))
        elif char.isupper():
            return chr((ord(char) - ord('A') + self.shift) % 26 + ord('A'))
        else:
            return char


class ROT47(ROT):
    def __init__(self):
        super().__init__(47)

    def rotate_char(self, char):
        return chr((ord(char) - 33 + self.shift) % 94 + 33)


class FileHandler:
    @staticmethod
    def save_to_file(filename, encrypted_text):
        with open(filename, 'a') as file:
            file.write(encrypted_text)

    @staticmethod
    def read_from_file(filename):
        with open(filename, 'r') as file:
            return file.read()


class InputReader:
    @staticmethod
    def read_input(prompt):
        while True:
            try:
                user_input = input()
                InputReader.validate_input(user_input)
                return user_input
            except ValueError as e:
                print(e)

    @staticmethod
    def validate_input(text):
        invalid = ['ą', 'ę', 'ó']
        for element in invalid:
            if element in text:
                raise ValueError(f"Invalid character '{element}' found in input.")


class Menu:
    def __init__(self):
        self.rot13 = ROT13()
        self.rot47 = ROT47()
        self.file_handler = FileHandler()
        self.input_reader = InputReader()
        self.encrypted_words = {}
        self.decrypted_text = ''

    def display_menu(self):
        print("==== Text Encryption Menu ====")
        print("1. Encrypt plain text (ROT47/ROT13)")
        print("2. Save encrypted texts to file")
        print("3. Decrypt encrypted text from file (ROT47/ROT13)")
        print("4. Print encrypted words stored in memory")
        print("5. Print everything from file")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = self.input_reader.read_input("Enter your choice: ")

            if choice == "1":
                self.encrypt_text()
            elif choice == "2":
                self.save_to_file()
            elif choice == "3":
                self.decrypt_from_file()
            elif choice == "4":
                self.print_encrypted_words()
            elif choice == '5':
                self.printing_file()
            elif choice == "6":
                run = False
            else:
                print("Invalid choice. Please try again.")

    def encrypt_text(self):
        text = self.input_reader.read_input("Enter the text to encrypt: ")
        encryption_choice = self.input_reader.read_input("Choose encryption method (ROT13/ROT47): ")

        if encryption_choice.lower() == "rot13":
            encrypted_text = self.rot13.encrypt(text)
            self.encrypted_words.update({'code': 'rot13', 'text': encrypted_text})
        elif encryption_choice.lower() == "rot47":
            encrypted_text = self.rot47.encrypt(text)
            self.encrypted_words.update({'code': 'rot47', 'text': encrypted_text})

    def save_to_file(self):
        item = f'typ kodowania: {self.encrypted_words["code"]},tekst: {self.encrypted_words["text"]}\n'
        self.file_handler.save_to_file('encrypted_texts', item)

    def decrypt_from_file(self):
        key = 'typ kodowania: '
        with open('encrypted_texts', 'r') as file:
            lines = file.readlines()
            for line in lines:
                code_type = line[len(key):].strip()[:5]

                pattern = r"typ kodowania: ([a-zA-Z0-9]+),tekst: ([a-zA-Z0-9]+)"
                match = re.search(pattern, line)
                encoded_text = match.group(2)
                if code_type == 'rot13':
                    self.rot13.decrypt(encoded_text)
                    self.decrypted_text = self.rot13.decrypt(encoded_text)

                elif code_type == 'rot47':
                    self.rot47.decrypt(encoded_text)
                    self.decrypted_text = self.rot47.decrypt(encoded_text)

    def printing_file(self):
        with open('encrypted_texts', 'r') as file:
            content = file.read()
        print(content)

    def print_encrypted_words(self):
        print(f'typ kodowania: {self.encrypted_words["code"]},tekst: {self.encrypted_words["text"]} ')


# menu = Menu()
# menu.run()
#
#
