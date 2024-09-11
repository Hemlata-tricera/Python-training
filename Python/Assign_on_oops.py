from abc import ABC, abstractmethod


# Abstract Base Class
class BankAccount(ABC):
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number  # Encapsulation: Protected attribute
        self._balance = initial_balance  # Encapsulation: Protected attribute

    @abstractmethod
    def deposit(self, amount):
        """ Abstract method to deposit money """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """ Abstract method to withdraw money """
        pass

    def get_balance(self):
        """ Return the current balance """
        return self._balance

    def get_account_number(self):
        """ Return the account number """
        return self._account_number


# Derived Class: CheckingAccount
class SavingAccount(BankAccount):
    def __init__(self, account_number, initial_balance, overdraft_limit):
        super().__init__(account_number, initial_balance)  # Inheritance: Initialize base class
        self._overdraft_limit = overdraft_limit  # Encapsulation: Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited Rs.{amount} into Checking Account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and (amount <= self._balance):
            self._balance -= amount
            print(f"Withdrew Rs.{amount} from Checking Account.")
        else:
            print("Insufficient balance or overdraft limit exceeded.")

    def get_overdraft_limit(self):
        """ Return the overdraft limit """
        return self._overdraft_limit
    def get_balance(self):
        """ Return the current balance """
        return self._balance



# Creating instances of CheckingAccount and SavingsAccount
hemlata = SavingAccount(account_number="123456", initial_balance=50000, overdraft_limit=200000)
print(hemlata.get_balance())
hemlata.deposit(10000)
print(hemlata.get_balance())
hemlata.withdraw(20000)
print(hemlata.get_balance())


