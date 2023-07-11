# Zadanie: Spróbuj odwzorować w kodzie powyższą implementację kont bankowych. Wykorzystaj klasę abstrakcyjną,
# metodę fabrykującą oraz utwórz symulacje trzech metod obiektów: validateUserIdentity(), calculateInterestRate(),
# registerAccount(). Symulacja ma polegać jedynie na wyświetlaniu określonych komunikatów.
import random
from abc import ABC


class Account(ABC):

    def __init__(self, name):
        self.name = name
        self.validateUserIdentity()


    def validateUserIdentity(self):
        print('user validated')


    def calculateInterestRate(self):
        print('calcuated interest')


    def registerAccount(self):
        print('account registered')


class PrivateAccount(Account):
    def created(self):
        print('utworzono konto osobiste')


class BusinessAccount(Account):
    def created(self):
        print('utworzono konto firmowe')


class AccountFactory:
    def get_account(self,account_type, name):
        if account_type == 'private':
            return PrivateAccount(name)
        elif account_type == 'business':
            return BusinessAccount(name)
        else:
            return None


factory = AccountFactory()
account = factory.get_account('private', 'Karol')

