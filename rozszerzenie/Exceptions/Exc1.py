# Przygotuj klasę FileHandler, która symulować będzie funkcjonalność obsługiwania plików w Javie.
# Ma ona przechowywać pola takie jak: file_path, no_connectors, max_file_size.
# Będa one ustawiane z poziomu odpowiednich setterów jak i konstruktora.
# Klasa ta ma dodatkowo przechowywać takie metody jak read_content, save_to_file, w których umieścisz, tzw.
# dummy printy (będziesz drukował dowolny tekst).
#
# Celem tego zadania nie jest stworzenie odpowiedniej logiki biznesowej dla klasy, tylko zaprojektowanie klasy,
# która będzie zwracała odpowiedni user-defined wyjątek w zależności od przekazania do obiektu klasy niewłaściwej danej,
# np. pustego stringa, który będzie miał być umieszczony pod polem file_path.
#
# Dodatkowe warunki:
# Wartość noConnector nie może przekroczyć wartości 10
# maxFileSize musi być zawsze liczbą czterocyfrową
file = open('test.txt', 'r')


class FileHandler:

    def __init__(self, file_path, no_connectors, max_file_size):
        self.__file_path = file_path
        self.__no_connectors = no_connectors
        self.__max_file_size = max_file_size
        self.read_content()
        self.save_to_file()

    def set_path(self, file_path):
        self.__file_path = file_path

    def set_connectors(self, no_connectors):
        self.__no_connectors = no_connectors

    def set_max(self, max_file_size):
        self.__max_file_size = max_file_size

    def read_content(self):
        if self.__no_connectors > 10:
            raise SmallerThan10(self.__no_connectors)
        else:
            print('read content')

    def save_to_file(self):
        if self.__max_file_size < 999:
            raise MinSize(self.__max_file_size)
        elif self.__max_file_size > 9999:
            raise MaxSize(self.__max_file_size)
        else:
            print(f'save to{self.__file_path} file')


class SmallerThan10(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Typed value of noConnector - {self.value} is bigger than 10!"


class MaxSize(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"file size {self.value} is too big!"


class MinSize(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"file size {self.value} is too small!"


dupa = FileHandler(file, 11, 666)

new_dict = {}

new_dict['dupa'] = 'nic'

new_list = []
for element in new_dict:
    new_list.append(new_dict[element])

new_list = [new_dict[element] for element in new_dict]



