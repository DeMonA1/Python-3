# mapattrs-slots.py: тестирует наследование атрибутов__slots__

from mapattrs import mapattrs, trace
class A (object) : __slots__ = ['a', 'b'] ; x = 1; у = 2
class В(A): __slots__ = ['b', 'c']
class C(A): x = 2
class D(В, C):
    z = 3
    def __init__ (self): self.name = 'Bob'
    
I = D()
trace(mapattrs(I, bysource=True))           # Также trace (mapattrs (I))
