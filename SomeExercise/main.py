class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def printName(self):
        return "{} {}".format(self.first, self.last)


p1 = Employee('Tom', 'Harry', 4000)
p2 = Employee('Jack', 'John', 5600)

print(p2.pay)
print(p1.printName())


