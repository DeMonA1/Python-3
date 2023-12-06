from abc import ABCMeta, abstractmethod
from typing import Any

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass

"""X=Super()"""

class Sub(Super): pass

"""X=Sub()"""

class Sub(Super):
    def action(self): print('spam')

X = Sub()
"""X.delegate()"""

class C:
    x = 33
    def m(self):
        x = 44
        self.x = 55

"""obj = C()
print(obj.x)
obj.m()
print(obj.x)"""

class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + 'not allowed')
        
"""x = AccessControl()
x.age = 40
print(x.age)"""

class Number:
    def __init__(self, val):
        self.val = val
    
    def __iadd__(self, other):
        self.val += other
        return self
"""y = Number([1])
y += [2]
print(y.val)"""

class Number:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        return Number(self.val + other)
    
class Callee:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('Called:', args, kwds)

"""C = Callee()
C(1,2,3,dict(a=1,b=5))"""

class C:
    data = 'spam'
    def __gt__(self,other):
        return self.data > other
    
    def __lt__(self, other):
        return self.data < other

X = C()
print(X>'ham')
print(X < 'ham')