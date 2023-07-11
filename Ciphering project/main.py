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
# zastosuj zasadę test driven development
# input przechowany w atrybucie\
import re


class ROT:
    def __init__(self, shift):
        """
        Shift is an attribute storing value of an offset relevant for each method of
        encrypting text rot13 i rot47
        """
        self.shift = shift

    def encrypt(self, text):
        """
        The encrypt function is part of the text encoding method, common to rot13 and rot47,
        the correct method is rotate_char appropriate for each encoding method, placed
        in the already appropriate classes inheriting from the ROT class
        """
        encrypted_text = ""
        for char in text:
            encrypted_char = self.rotate_char(char)
            encrypted_text += encrypted_char
        encrypted_tekst_to_save = encrypted_text
        return encrypted_text

    def decrypt(self, text):
        """
        The rot13 and rot47 methods are symmetric, that is, you only need to use
        a second time on theencoded text with the same method to decode it
        """
        print(self.encrypt(text))
        return self.encrypt(text)

class ROT13(ROT):
    def __init__(self):
        super().__init__(13)

    def rotate_char(self, char):
        """
        Method that moves each character in the encoded text according to
        the selected method
        """
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
        """
        Method that moves each character in the encoded text according to
        the selected method
        """
        ascii_val = ord(char)
        if 33 <= ascii_val <= 126:
            return chr(((ascii_val - 33) - self.shift) % 94 + 33)
        return char


class FileHandler:
    @staticmethod
    def save_to_file(filename, encrypted_text):
        """
        A method that saves the encoded text in the appropriate file
        """
        with open(filename, 'a') as file:
            file.write(encrypted_text)

    @staticmethod
    def read_from_file(filename):
        """
        Method which reads everything from file with encoded texts
        """
        with open(filename, 'r') as file:
            return file.read()


class InputReader:
    @staticmethod
    def read_input(prompt):
        """
        Method allowing to take user's input for various requests
        """
        while True:
            try:
                user_input = input()
                InputReader.validate_input(user_input)
                return user_input
            except ValueError as e:
                print(e)

    @staticmethod
    def validate_input(text):
        """
        Checking if user's input doesn't contain forbidden signs
        """
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
        """
        Menu visible for user
        """
        print("==== Text Encryption Menu ====")
        print("1. Encrypt plain text (ROT47/ROT13)")
        print("2. Save encrypted texts to file")
        print("3. Decrypt encrypted text from file (ROT47/ROT13)")
        print("4. Print encrypted words stored in memory")
        print("5. Print everything from file")
        print("6. Exit")

    def run(self):
        """
        Loop that takes user's choice with read_input method and starts proper
        method
        """
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
        """
        Taking text and coding method user want's to use to encrypt, then launching
        chosen method with desired text as attribute
        """
        text = self.input_reader.read_input("Enter the text to encrypt: ")
        encryption_choice = self.input_reader.read_input("Choose encryption method (ROT13/ROT47): ")

        if encryption_choice.lower() == "rot13":
            encrypted_text = self.rot13.encrypt(text)
            self.encrypted_words.update({'code': 'rot13', 'text': encrypted_text})
        elif encryption_choice.lower() == "rot47":
            encrypted_text = self.rot47.encrypt(text)
            self.encrypted_words.update({'code': 'rot47', 'text': encrypted_text})

    def save_to_file(self):
        """
        Saving encoded tekst to 'encrypted_texts' file in specified form
        """
        item = f'typ kodowania: {self.encrypted_words["code"]},tekst: {self.encrypted_words["text"]}\n'
        self.file_handler.save_to_file('encrypted_texts', item)

    def decrypt_from_file(self):
        """
        decoding encrypted texts from file by using decrypt method, to choose proper
        method(rot13 or rot47), we read from file with RegEx
        """
        key = 'typ kodowania: '
        with open('encrypted_texts', 'r') as file:
            lines = file.readlines()
            for line in lines:
                code_type = line[len(key):].strip()[:5]

                pattern = r"typ kodowania: ([a-zA-Z0-9]+),tekst: ([\b\S+\b]+)"
                match = re.search(pattern, line)
                encoded_text = match.group(2)
                if code_type == 'rot13':
                    # self.rot13.decrypt(encoded_text)
                    self.decrypted_text = self.rot13.decrypt(encoded_text)

                elif code_type == 'rot47':
                    # self.rot47.decrypt(encoded_text)
                    self.decrypted_text = self.rot47.decrypt(encoded_text)

    def printing_file(self):
        """
        Printing everything from file with texts
        """
        with open('encrypted_texts', 'r') as file:
            content = file.read()
        print(content)

    def print_encrypted_words(self):
        """
        printing encrypted word with encrypting method saved in memory as encrypted_words
        """
        print(f'typ kodowania: {self.encrypted_words["code"]},tekst: {self.encrypted_words["text"]} ')


menu = Menu()
menu.run()
