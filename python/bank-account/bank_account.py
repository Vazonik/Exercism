import threading

class BankAccount:
    def __init__(self):
        self.isOpen = False
        self.balance = 0
        self.lock = threading.Lock()

    def get_balance(self):
        if self.isOpen:
            return self.balance
        else:
            raise ValueError(".+")

    def open(self):
        if not self.isOpen:
            self.isOpen = True
            self.balance = 0
        else:
            raise ValueError(".+")

    def deposit(self, amount):
        if self.isOpen and amount > 0:
            self.lock.acquire()
            self.balance += amount
            self.lock.release()
        else:
            raise ValueError(".+")

    def withdraw(self, amount):
        if self.isOpen and amount > 0 and self.balance - amount >= 0:
            self.lock.acquire()
            self.balance -= amount
            self.lock.release()
        else:
            raise ValueError(".+")

    def close(self):
        if self.isOpen:
            self.isOpen = False
        else:
            raise ValueError(".+")
