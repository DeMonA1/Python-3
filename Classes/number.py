class Number:
    def __init__(self, start) -> None:
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)
x = Number(5)
x -= 2
print(x.data)
    
class Indexer:
    def __getitem__(self, index):
        return index ** 2
X = Indexer()
"""print(X[2])
for i in range(5):
    print(X[i])"""
L = [5,6,7,8,9]
"""print(L[2:4])
print(L[1:])
print(L[:-1])
print(L[::2])"""
"""print(L[slice(2,4)])
print(L[slice(1, None)])
print(L[slice(None, -1)])"""

class Indexer:
    data = [5,6,7,8,9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]
x = Indexer()
"""print(x[2:4])
print([3])"""

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]
x= StepperIndex()
x.data = 'Spam'
print(x[1])
for item in x:
    print(item, end=' ')
print(list(map(str.upper, x)))