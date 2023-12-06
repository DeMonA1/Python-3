import lister
lister.ListInstance  # использовать специфический класс, выводящий атрибуты
lister.Lister       # Использовать стандартный класс Lister
from lister import Lister     # Использовать стандартный класс Lister
Lister
from lister import ListInstance as Lister   # Использовать псевдоним Lister

from setwrapper import Set
x = Set([1,3,5,7])
"""print(x.union(Set([1,4,7])))
print(x | Set([1,4,6]))"""

class C():
    data = 'spam'
    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)
X = C()
"""X[0]  """     # Error
"""print(X)"""

class C: pass
X = C()
X.normal = lambda: 99
"""print(X.normal())"""
X.__add__ = lambda y: 88 + y
"""print(X.__add__(1))"""

class C(object):
    def __getattr__(self, name): print(name)
X = C()
"""X.normal
X.__add__"""
"""X + 1"""  # Error

class C:
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)
X = C()
"""X.__getitem__(1)"""
"""X.__add__('eggs')"""
"""X + > X[1]"""  #Error

class C:
    data = 'spam'
    def __getattr__(self, name):        # Перехватывать нормальные имена
        print('getattr: ' + name)
        return getattr(self.data,name)
    
    def __getitem__(self, i):           # Переопределить встроенные операции
        print('getitem: ' + str(i))
        return self.data[i]             # Выполнить выражение или getattr
    
    def __add__(self, other):
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)

"""X = C()
X.upper
X.upper()
X[1]                # Встроенная операция(неявная)
X.__getitem__(1)     # Традиционный эквивалент(явный)
type(X).__getitem__(X, 1)   # Эквивалент нового стиля
X + 'eggs'                  # То же самое для + и остальных
X.__add__('eggs')
type(X).__add__(X, 'eggs')"""

class A:pass
class B(A):pass     # Ромбы: для классов нового стиля порядок отличается
class C(A):pass     # Поиск сначала в ширину на нижних уровнях
class D(B,C): pass
"""print(D.__mro__)
print(A.__bases__)"""
class X:pass
class Y: pass
class A(X): pass
class B(Y): pass
class D(A, B): attr = 1
"""o = D()
print(D.__mro__)
print(dir(D))"""

from mapattrs import trace, dflr, inheritance, mapattrs
from testmixin0 import Sub
I = Sub()
"""trace(dflr(I.__class__))
trace(inheritance(I))
trace(mapattrs(I))
amap = mapattrs(I, withobject=True, bysource=True)
trace(amap)"""

class limiter(object):
    __slots__ = ['age', 'name', 'job']
x = limiter()
# x.age  => AttributeError
x.age = 40
"""print(x.age)"""
# x.ape = 1000 Has no attr

class C:
    __slots__ = ['a', 'b']
x = C()
x.a = 1
"""print(x.a)"""
# x.__dict__ has no this attr
getattr(x, 'a') # 1
setattr(x, 'b', 2)
x.b  # 2
'a' in dir(x) # True
'b' in dir(x) # True

class D:
    __slots__ = ['a', 'b']
    def __init__(self):
        self.d = 4          # В отсутствие__diet__добавлять новые имена невозможно
# x = D()  D has no attr d 

class D:
    __slots__ = ['a', 'b', '__dict__']  #  Указание__ diet__ для его включения
    c = 3                       #  Атрибуты класса работают нормально
    def __init__(self):
        self.d = 4          #  d хранится в__diet__ , а является слотом
x = D()
x.d # 4
x.c # 3
# x.a  error 
x.a = 1
x.b = 2
"""print(x.__dict__)
print(x.__slots__)
print(getattr(x, 'a'), getattr(x, 'c')) """

class E:
    __slots__ = ['c', 'd']
class D(E):
    __slots__ = ['a', '__dict__']
x = D()
x.a = 1; x.b = 2; x.c = 3
"""print(x.a, x.c)
print(dir(x))
print(x.__dict__)"""

class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self, data):
        self.c = data
i = Slotful(3)
i.a, i.b = 1,2
"""print(i.a, i.b, i.c)
print(i.__dict__)
print([x for x in dir(i) if not x.startswith('__')])
print(i.__dict__['c'])
print(getattr(i, 'c'), getattr(i, 'a'))"""

