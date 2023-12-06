class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1
        x(42)
# Eggs().m2()

class Selfless:
    def __init__(self, data):
        self.data = data
    
    def selfless(arg1, arg2):
        return arg1 + arg2
    
    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2
"""X = Selfless(2)
print(X.normal(3,4))
print(Selfless.normal(X,3,4))
print(Selfless.selfless(3,4))"""

class Number:
    def __init__(self, base):
        self.base = base
    
    def double(self):
        return self.base * 2
    
    def triple(self):
        return self.base * 3
"""x = Number(2)
y = Number(3)
z = Number(4)
print(x.double())
acts = [x.double, y.double, y.triple, z.double]
for act in acts:
    print(act)
bound = x.double
print(bound.__self__, bound.__func__)
print(bound.__self__.base)
print(bound())"""

def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val
    
    def __call__(self, arg):
        return self.val + arg
    
class Product:
    def __init__(self, val):
        self.val = val
    
    def method(self, arg):
        return self.val * arg
    
sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]
"""for act in actions:
    print(act(5))
print(actions[-1](5))
print([act(5) for act in actions])
print(list(map(lambda act: act(5), actions)))"""

class Negate:
    def __init__(self, val):
        self.val = -val
    
    def __repr__(self):
        return str(self.val)
    
actions = [square, sobject, pobject.method, Negate]
"""for act in actions:
    print(act(5))"""

"""# ex_1
classname = ... извлечь из конфигурационного файла и произвести разбор...
classarg = ... извлечь из конфигурационного файла и произвести разбор...
import streamtypes   # настраиваемый код
aClass = getattr(streamtypes, classname)    #извлечь из модуля
reader = factory(aClass, classarg)  #или aClss(classarg)
processor(reader, ...)
"""
import listinstance
class C(listinstance.ListInstance): pass
"""x=C()
x.a, x.b, x.c = 1,2,3
print(x)"""

class C: pass
class B(C): pass
# C.__bases__ = (B,) ошибка бесконечный цикл

from listtree import ListTree
from tkinter import Button              # Оба класса имеют метод __str__
class MyButton(ListTree, Button): pass  # ListTree первый: испоьзуется его метод __str__
B = MyButton(text = 'spam')
open('savetree.txt', 'w').write(str(B)) # Сохранить файл для просмотра в будущем
"""print(len(open('savetree.txt').readlines()))   # Строк в файле
print(B)"""
S = str(B)
"""print(S[:1000])"""