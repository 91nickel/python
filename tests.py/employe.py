class Employee:
    def __init__(self, name, last_name, pay):
        self.name = name
        self.last_name = last_name
        self.pay = pay

    def give_raise(self, count=5000):
        self.pay += count
