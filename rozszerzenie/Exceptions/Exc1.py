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
file = open(test.txt, 'r')
class FileHandler:

    def __init__(self, file_path, no_connectors, max_file_size):
        self.__file_path = file_path
        self.__no_connectors = no_connectors
        self.__max_file_size = max_file_size

    def set_path(self, file_path):
        self.__file_path = file_path

    def set_connectors(self, no_connectors):
        self.__no_connectors = no_connectors

    def set_max(self, max_file_size):
        self.__max_file_size = max_file_size

    def read_content(self):
        print('read content')

    def save_to_file(self):
        print('save to file')

dupa = FileHandler()
