# Stwórz klasę KontoBankowe, która będzie reprezentować konto bankowe z metodami wplac(suma) oraz wyplac(suma).
# Konto bankowe ma mieć atrybut stan_konta oraz metodę stan(), która zwraca aktualny stan konta. Następnie stwórz klasę
# KontoZakladkowe, dziedziczącą po klasie KontoBankowe, z atrybutem oprocentowanie i metodą nalicz_odsetki(),
# która zwiększa stan konta o kwotę naliczonych odsetek (według podanego oprocentowania) oraz zwraca naliczoną kwotę.
# Klasa KontoBankowe oraz KontoZakladkowe powinny wywoływać wyjątek ValueError, gdy podana kwota wypłaty jest większa
# niż aktualny stan konta.

class BankAccount():
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self):
        amount = int(input('podaj wpłacaną kwotę: '))
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise ValueError('nie masz wystarczających środków na koncie')
        self.account_balance -= amount

    @property
    def balance(self):
        return self.account_balance


class BookmarkAccount(BankAccount):
    def __init__(self, interest=0.05, account_balance=0):
        super().__init__(account_balance)
        self.interest = interest

    def charge_interest_amount(self):
        print(self.account_balance)
        self.account_balance += self.account_balance*self.interest
        print(self.account_balance)


account = BankAccount(120)
bookmark_account = BookmarkAccount(account_balance=100)

account.deposit()
account.withdraw(100)
print(account.balance)

bookmark_account.charge_interest_amount()
bookmark_account.deposit()
bookmark_account.charge_interest_amount()

