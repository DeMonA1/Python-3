class C1():

    def setname(self,who):
        self.name = who

I1 = C1()
I1.setname('bob')


class C1():
    def __init__(self, name) -> None:
        self.who = name
I1=C1('bob')


class FirstClass:

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):

    def display(self):
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):

    def __init__(self,value) -> None:
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)
    
    def __str__(self) -> str:
        return '[ThirdClass: %s]' % self.data
    
    def mul(self, other):
        self.data *= other

#реализация словаря на основе объекта класса
class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self. jobs)

rec1 = Person('Bob', ['dev','mgr'], 40.6)
rec2 = Person('Sue', ['dev', 'cto'])
print(rec1.jobs, rec2.info())







a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
print(b)
a.mul(3)
print(a)