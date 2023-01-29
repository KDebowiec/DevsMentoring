# Stwórz Pythonową klasę BankAccount, która reprezentować będzie konto bankowe zawierające takie informacje jak:
# numer_konta, nazwa właściciela konta, stan konta.
# Stwórz konstruktor odpowiednio uzupełniający pola.
# Napisz metodę deposit(), która przyjmować będzie kwotę, jaką chcesz wpłacić na konto.
# Dodaj założenie, że za każde wpłacone 100 zł, pobierana będzie prowizja równa 2 zł.
# Stwórz metodę withdraw(), która przyjmować będzie jako parametr kwotę, którą chcesz wypłacić z konta.
# Program ma wyświetlać odpowiedni komunikat, gdy niemożliwe jest wypłacanie wskazanej ilości pieniędzy
# (przykładowo z powodu braku wystarczającej ilości środków na koncie).
# Napisz metodę change_ownership(), która przyjmować będzie imię nowego właściciela konta i będzie aplikowała
# tę zmianę w obiekcie klasy.
# Stwórz metodę display(), która będzie wyświetlać wszystkie informacje o koncie.



class Account:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self):
        cash_in = int(input('podaj wpłacaną kwote: '))
        self.balance += cash_in - 2
        print(f"Twój stan konta to teraz {self.balance}")

    def withdraw(self):
        cash_out = int(input('podaj wypłacaną kwotę'))

        if cash_out <= self.balance:
            self.balance -= cash_out
            print(f"Twój stan konta to teraz {self.balance}")
        else:
            print('nie masz wystarczających środków na koncie, wypierdalaj')

    def change_ownership(self):
        new_owner = input('podaj nowego właściciela konta: ')
        self.owner = new_owner

    def display(self):
        print(f'właścicielem konta o numerze {self.number} jest {self.owner}, stan konta to {self.balance}')


account = Account(23456765432345, "Karol", 1000000)

run = True

while run: # wrzucić do metody w klasie
    print("wprowadź 1 aby wpłacić pieniądze na konto: ")
    print("wprowadź 2 aby wypłacić pieniądze: ")
    print("wprowadź 3 aby zmienić właściciela: ")
    print("wprowadź 4 aby uzyskać informacje o koncie: ")
    print("wprowadź 5 aby zakończyć: ")
    choice = int(input("wybór użytkownika: "))

    if choice == 1:
        account.deposit()
    elif choice == 2:
        account.withdraw()
    elif choice == 3:
        account.change_ownership()
    elif choice == 4:
        account.display()
    elif choice == 5:
        run = False