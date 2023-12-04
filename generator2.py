import os

def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i
list(both(5))
# equivalent
def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))
list(both(5))
':'.join(str(i) for i in both(5))

for (root, subs, files) in os.walk('.'):
    #проход по каталогам
    for name in files:
        if name.startswith('call'):
            print(root,name)

def f(a, b, c): print('%s, %s, and %s' % (a, b, c))
"""print(*range(3))"""
D = dict(a='bob', b='dev', c=40.5)
"""print(f(**D))
print(f(*D))
print(*D.values())"""

list(print(x.upper(), end=' ') for x in 'spam') #S P A M [None, None, None, None]
print(*(x.upper() for x in 'spam'))