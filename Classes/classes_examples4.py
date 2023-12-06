class Operators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError
x = Operators()
"""print(x.age)"""

class properties:
    def getage(self):
        return 40
    age = property(getage, None, None, None)
x = properties()
"""x.age"""

class properties:
    def getage(self):
        return 40
    def setage(self, value):
        print('set age: %s' % value)
        self._age = value
    age = property(getage, setage, None, 'adsda')
x = properties()
"""x.age = 'banana'
print(x._age)  # banana
print(x.age)   # 40"""


class Operators:
    def __getattr__(self, name):
        if name  == 'age':
            return 40
        else:
            raise AttributeError(name)
    
    def __setattr__(self, name, value):
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value
x = Operators()
"""print(x.age)
x.age = 41
print(x._age)"""

# descriptor
class AgeDesc:
    def __get__(self, instance, owner): return 40
    def __set__(self, instance, value): instance._age = value

class Descriptors:
    age = AgeDesc()
x = Descriptors()
"""print(x.age)
x.age = 42
print(x._age)"""

from spam_class import Spam
"""a = Spam()
b = Spam()"""
"""Spam.printNumInstances()"""
    
"""def printNumInstances():
    print('Number if instances created: %s' % Spam.numInstances)"""

"""class Spam: 
    numInstances = 0
    def __init__(Self):
        Spam.numInstances = Spam.numInstances + 1
a = Spam()
b = Spam()"""
"""printNumInstances()"""

from spam_static import Spam, Sub
a = Sub()
b = Sub()
"""a.printNuminstances()
Sub.printNuminstances()
Spam.printNumInstances()
"""

"""from spam_class import Spam, Sub, Other
x = Sub()
y = Spam()
x.printNumInstances()
Sub.printNumInstances()
y.printNumInstances()"""

from spam_class2 import Spam, Sub, Other
x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(),Other()
"""print(x.numInstances, y1.numInstances, z1.numInstances)
print(Spam.numInstances, Sub.numInstances, Other.numInstances)"""

def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self, a,b,c): return a+b+c

"""x = C()
print(x.spam(1,2,3))
print(x.spam('a','b','c'))"""

class C:
    def act(self):
        print('spam')
    
class D(C):
    def act(self):
        C.act(self)
        print('eggs')
"""X = D()
X.act()"""

class C:
    def act(self):
        print('spam')
    
class D(C):
    def act(self):
        super().act()
        print('eggs')
"""X = D()
X.act()"""
class E(C):
    def method(self):
        proxy = super()
        print(proxy)
        proxy.act()
"""E().method()"""

class A:
    def act(self): print('A')

class B:
    def act(self): print('B')

class C(B,A):
    def act(self):
        super().act()
"""X = C()
X.act()"""

class C:
    def __getitem__(self, ix):
        print('C index')

class D(C):
    def __getitem__(self, ix):
        print('D index')
        C.__getitem__(self, ix)
        super().__getitem__(ix)
"""X = C()
X[99]
X = D()
X[99]"""

class C:
    shared = []
    def __init__(self):
        self.perobj = []
x = C()
y = C()
"""print(y.shared, y.perobj)"""
x.shared.append('spam')
y.perobj.append('spam')
"""print(C.shared)
x.shared = 1
print(x.shared, y.shared)
print(C.shared)
print(x.__class__)"""

def generate():
    class Spam:
        count = 1
        def method(self):
            print(Spam.count)
    return Spam()
x = generate()
x.method()