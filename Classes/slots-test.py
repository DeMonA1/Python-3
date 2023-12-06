import timeit

base = """
Is = []
for i in range(1000):
    x = C()
    x.a = 1; x.b = 2; x.c = 3; x.d =4
    t = x.a + x.b + x.c + x.d
    Is.append(x)
"""
stmt = """
class C(object):
    __slots__=['a', 'b', 'c', 'd']
"""
print('Slots =>', end=' ')
print(min(timeit.repeat(stmt, number=1000, repeat=3)))
stmt = """
class C(object):
    pass
""" + base
print('Nonslots =>', end=' ')
print(min(timeit.repeat(stmt, number=1000, repeat=3)))