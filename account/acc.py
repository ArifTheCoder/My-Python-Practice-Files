class Account:

    def __init__(self, filePath):

        self.filePath = filePath

        with open(filePath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filePath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    type = "Checking"

    def __init__(self, filePath, fee):
        Account.__init__(self, filePath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


tom_checking = Checking("tom.txt", 2)
tom_checking.transfer(320)
tom_checking.commit()
print(tom_checking.balance)
print(tom_checking.type)

jerry_checking = Checking("jerry.txt", 2)
jerry_checking.transfer(120)
jerry_checking.commit()
print(jerry_checking.balance)
print(jerry_checking.type)
