class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')

class Subject:
    attr = Descriptor()

X = Subject()
X.attr
Subject.attr

#======================================================

class D:
    def __get__(*args): print('get')

class C:
    a = D()

X = C()
X.a
C.a
X.a = 99
X.a
list(X.__dict__.keys())
Y = C()
Y.a
C.a

"""class D:
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')

class C:
    a = D()

X = C()
X.a
X.a = 99"""

#========================================================

class Name:
    'name descriptor docs'
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    
    def __delete__(self, instance):
        print('remove...')
        del instance._name
    
class Person:
    def __init__(self, name):
        self._name = name 
    name = Name()
    
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name 

print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
print(Name.__doc__)

#========================================================

class DescSquare:
    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2
    
    def __set__(self, instance, value):
        self.value = value
    
class Client1:
    X = DescSquare(3)

class Client2:
    X = DescSquare(32)

c1 = Client1()
c2 = Client2()

print(c1.X)
c1.X = 4
print(c1.X)
print(c2.X)

#==============================================================

class DescState:
    def __init__(self, value):
        self.value = value
    
    def __get__ (self, instance, owner):
        print('DescState get')
        return self.value * 10
    
    def __set__(self, instance, value):
        print('DescState set')
        self.value = value

class CalcAttrs:
    X = DescState(2)
    Y = 3
    def __init__(self):
        self.Z = 4

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

#==============================================

class InstState:
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._Y * 100
    
    def __set__(self, instance, value):
        print('InstState set')
        instance._Y = value

class CalcAttrs:
    X = DescState(2)
    Y = InstState()
    def __init__(self):
        self._Y = 3
        self.Z = 4

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

#====================================================

class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)
    
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person:
    def getName(self): pass
    def setName(self, value): pass
    name = Property(getName, setName)

#========================================================

class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2
    
    def __set__(self, instance, value):
        instance._square = value
    
class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3
    
class Powers:
    square = DescSquare()
    cube = DescCube()
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)

#================================================================

class CardHolder:
    acctlen = 8                                             # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                                    # Instance data
        self.name = name                                    # These trigger __set__ calls too
        self.age = age                                      # __X not needed: in descriptor
        self.addr = addr                                    # addr is not managed
                                                            # remain has no data

    class Name:
        def __get__(self, instance, owner):                 # Class names: CardHolder locals
            return self.name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age                                 # Use descriptor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:              # Use instance class data
                raise TypeError('invald acct number')
            else:
                self.acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age        # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')            # Else set allowed here
    remain = Remain()
