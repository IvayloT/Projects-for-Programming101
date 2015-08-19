class BankAccount():
    def __init__(self, name, balance, currency):
        self.name = str(name)
        self.balance = balance
        self.currency = str(currency)
        self.history = []

        self.make_history("Account was created")

    def __str__(self):
        return "Bank account for {} with balance of {} {}" .format(self.name, self.balance, self.currency)

    def __repr__(self):
        return self.__str__()


    def deposit(self, amount):
        self.balance += amount

    def currency(self):
        return self.currency

    def holder(self):
        return self.name

    def balance(self):
        self.make_history("balance check -> {}{}" .format(self.balance, self.currency))

        return self.balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            self.balance - amount >= 0
            self.balance -= amount
            return True


    def transferTo(self, account, amount):
        if (self.balance >= amount):
            self.balance -= amount
            account.balance += amount
            return True
        else:
            return False
