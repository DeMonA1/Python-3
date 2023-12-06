class Commuter1:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val
"""x = Commuter1(88)
y = Commuter1(99)
print(x + 1)
print(1 + y)
print(x + y)"""

class Commuter2:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    def __radd__(self, other):
        return self.__add__(other)
    
class Commuter3:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val  + other
    
    def __radd__(self, other):
        return self + other
    

class Commuter4:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    __radd__ = __add__     #псевдоним: исключить посредника


class Commuter5:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):
            other = other.val
        return Commuter5(self.val + other)
    
    def __radd__(self, other):
        return Commuter5(self.val + other)
    
    def __str__(self):
        return '<Commuter5: %s>' % self.val
    
if __name__ == '__main__':
    for klass in (Commuter1, Commuter2, Commuter3, Commuter4, Commuter5):
        print('-' * 60)
        x = klass(88)
        y = klass(99)
        print(x + 1)
        print(1 + y)
        print(x + y)
            