from typing import Any


class Catcher:
    def __getattr__(self, name):
        print('Get:', name)
    
    def __setattr__(self, name, value):
        print('Set:', name, value)
    
X = Catcher()
X.job
X.pay
X.pay = 99

#==============================================================

class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    
    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)
    
#===============================================================

def __getattribute__(self, name):
    x = object.__getattribute__(self,'other')

def __setattr__(self, name, value):
    self.__dict__['other'] = value

def __setattr__(self, name, value):
    object.__setattr__(self, 'other', value)

#===================================================================

class Person:
    def __init__(self, name):
        self._name = name
    
    def __getattr__(self, attr):
        if attr == 'name':
            print('fetch...')
            return self._name
        else:
            raise AttributeError(attr)
        
    def __setattr__(self, attr, value):
        if attr == 'name':
            print('change...')
            attr = '_name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        if attr == 'name':
            print('remove...')
            attr = '_name'
        del self.__dict__[attr]

bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name 

print('-'*20)
sue = Person('Sue Jones')
print(sue.name)
# print(Person.name.__doc__)

#======================================================

class AttrSquare:
    def __init__(self, start):
        self.value = start
    
    def __getattr__(self, attr):
        if attr == 'X':
            return self.value ** 2
        else:
            raise AttributeError(attr)
    
    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value

A = AttrSquare(3)
B = AttrSquare(32)

print(A.X)
A.X = 4
print(A.X)
print(B.X)

class AttrSquare:
    def __init__(self, start):
        self.value = start
    
    def __getattribute__(self, attr):
        if attr == 'X':
            return object.__getattribute__(self, 'value') ** 2
        else:
            return object.__getattribute__(self, attr)
    
    def __setattr__(self, attr, value):
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)

#=============================================

class GetAttr:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    
    def __getattr__(self, attr):
        print('get: ' + attr)
        return 3
    
X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)

print('- '*20)

class GetAttribute:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    
    def __getattribute__(self, attr):
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)

#==================================================

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        
        elif name == 'cube':
            return self._cube ** 3
        
        else:
            raise TypeError('unknown attr:' + name)
        
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        
        else:
            self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)

#==================================================

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    
    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        
        else:
            return object.__getattribute__(self, name)
        
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        
        else:
            self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)

# ==========================================================

class GetAttr:
    eggs = 88
    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42
    
    def __getattr__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute:
    eggs = 88
    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42
    
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattribute str]'
        else:
            return lambda *args: None  

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '=')) 

    X = Class()
    X.eggs
    X.spam
    X.other
    len(X)

    try:
        X[0]
    except:
        print('fail []')
    
    try:
        X + 99
    except:
        print('fail +')
    
    try:
        X()
    except:
        print('fail ()')
    X.__call__()

    print(X.__str__())
    print(X)

#==========================================================

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
    
class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def __getattribute__(self, attr):
        print('**', attr)
        person = object.__getattribute__(self, 'person')
        if attr == 'giveRaise':
            return lambda percent: person.giveRaise(percent+.10)
        else:
            return getattr(person, attr)
    def __str__(self):
        person = object.__getattribute__(self, 'person')
        return str(person)
    
"""    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)
    def __str__(self):
        return str(self.person)
    def __getattr__(self, attr):
        return getattr(self.person, attr)"""
    
if __name__ =='__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    print(tom.lastName())
    tom.giveRaise(.10)
    print(tom)

#================================================================================

class CardHolder:
    acctlen = 8 # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct        # Instance data
        self.name = name        # These trigger __setattr__ too
        self.age = age          # _acct not mangled: name tested
        self.addr = addr        # addr is not managed
                                # remain has no data
                                
    def __getattr__(self, name):
        if name == 'acct':                  # On undefined attr fetches
            return self._acct[:-3] + '***'     # name, age, addr are defined
        elif name == 'remain':
            return self.retireage - self.age   # Doesn't trigger __getattr__
        else:
            raise AttributeError(name)
        
    def __setattr__(self, name, value):
        if name == 'name':                          # On all attr assignments
            value = value.lower().replace(' ', '_')         # addr stored directly
        elif name == 'age':                         # acct mangled to _acct
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value             # Avoid loopin

#===================================================================================

class CardHolder:
    acctlen = 8 # Class data
    retireage = 59.5
    def __init__(self, acct, name, age, addr):
        self.acct = acct            # Instance data
        self.name = name        # These trigger __setattr__ too
        self.age = age              # acct not mangled: name tested
        self.addr = addr                # addr is not managed
                                        # remain has no data
    def __getattribute__(self, name):
        superget = object.__getattribute__      # Don't loop: one level up
        if name == 'acct':                          # On all attr fetches
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name) # name, age, addr: stored
    def __setattr__(self, name, value):
        if name == 'name': # On all attr assignments
            value = value.lower().replace(' ', '_') # addr stored directly
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value # Avoid loops, orig names