class Person:

    def __init__(self,name,job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def __repr__(self) -> str:
        return '[Pesrson: %s, %s]' % (self.name, self.pay)
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager:
    def __init__(self,name,pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self) -> str:
        return str(self.person)



if __name__ == '__main__':
    bob = Person('bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 10000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)