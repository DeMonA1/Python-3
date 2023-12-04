def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:
    def __init__(self, x, y):
        self.attr = 'spam'

x = C(6,7)
print(x.attr)

#===================================================================

def d1(F): return F
def d2(F): return F
def d3(F): return F

@d1
@d2
@d3
def func():         # func = d1(d2(d3(func)))
    print('spam')

func()              # Prints "spam"

#========================================================================

def d1(F): return lambda: 'X' + F()
def d2(F): return lambda: 'Y' + F()
def d3(F): return lambda: 'Z' + F()

@d1
@d2
@d3
def func():         # func = d1(d2(d3(func)))
    return 'spam'

print(func())       # Prints "XYZspam"

#=======================================================

class tracer:
    def __init__(self, func):       # On @ decoration: save original func
        self.calls = 0
        self.func = func
    def __call__(self, *args):      # On later calls: run original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)
@tracer
def spam(a, b, c):          # spam = tracer(spam)
    print(a + b + c)           # Wraps spam in a decorator object

spam(1,2,3)          #Really calls the tracer wrapper object
spam('a','b','c')            #Invokes __call__ in class
print(spam.calls)           # Number calls in wrapper state information
print(spam)

#====================================================

calls = 0
def tracer(func, *args):
    global calls
    calls += 1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)
def spam(a, b, c):
    print(a, b, c)

spam(1,2,3)             # Normal non-traced call: accidental?
tracer(spam,1,2,3)      # Special traced call without decorators

#=========================================================

class tracer:                               # State via instance attributes
    def __init__(self, func):               # On @ decorator
        self.calls = 0                      # Save func for later call
        self.func = func
    def __call__(self, *args, **kwargs):    # On call to original function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    
@tracer
def spam(a, b, c):          # Same as: spam = tracer(spam)
    print(a + b + c)        # Triggers tracer.__init__

@tracer
def eggs(x, y):             # Same as: eggs = tracer(eggs)
    print(x ** y)           # Wraps eggs in a tracer object

spam(1, 2, 3)               # Really calls tracer instance: runs tracer.__call__
spam(a=4, b=5, c=6)         # spam is an instance attribute

eggs(2, 16)                 # Really calls tracer instance, self.func is eggs
eggs(4, y=4)                # self.calls is per-function here (need 3.0 nonlocal)

#=======================================================

calls = 0
def tracer(func):                   # State via enclosing scope and global
    def wrapper(*args, **kwargs):   # Instead of class attributes
        global calls                # calls is global, not per-function
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper
@tracer
def spam(a, b, c):                  # Same as: spam = tracer(spam)
    print(a + b + c)
@tracer
def eggs(x, y):                     # Same as: eggs = tracer(eggs)
    print(x ** y)
spam(1, 2, 3)                       # Really calls wrapper, bound to func
spam(a=4, b=5, c=6)                 # wrapper calls spam
eggs(2, 16)                         # Really calls wrapper, bound to eggs
eggs(4, y=4)                        # Global calls is not per-function here

#===================================================

def tracer(func):                        # State via enclosing scope and nonlocal
    calls = 0                            # Instead of class attrs or global
    def wrapper(*args, **kwargs):        # calls is per-function, not globa
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):              # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                 # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)                   # Really calls wrapper, bound to func
spam(a=4, b=5, c=6)             # wrapper calls spam

eggs(2, 16)                     # Really calls wrapper, bound to eggs
eggs(4, y=4)                    # Nonlocal calls _is_ not per-function here

def tracer(func):                       # State via enclosing scope and func attr
    def wrapper(*args, **kwargs):       # calls is per-function, not global
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

#========================================================

# A decorator for both functions and methods

def tracer(func):                   # Use function, not class with __call__
    calls = 0                       # Else "self" is decorator instance only!
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

# Applies to simple functions

@tracer
def spam(a, b, c):               # spam = tracer(spam)
    print(a + b + c)             # onCall remembers spam

spam(1, 2, 3)                    # Runs onCall(1, 2, 3)
spam(a=4, b=5, c=6)

# Applies to class method functions too!

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @tracer
    def giveRaise(self, percent):           # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)         # onCall remembers giveRaise
    @tracer
    def lastName(self):                     # lastName = tracer(lastName)
        return self.name.split()[-1]
    
print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)                          # Runs onCall(sue, .10)
print(sue.pay)
print(bob.lastName(), sue.lastName())        # Runs onCall(bob), lastName in scopes

#=======================================================

"""class tracer(object):
    def __init__(self, func):                   # On @ decorator
        self.calls = 0                          # Save func for later call
        self.func = func
    def __call__(self, *args, **kwargs):        # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):         # On method attribute fetch
        return wrapper(self, instance)"""
class tracer:
    def __init__(self, func):                   # On @ decorator
        self.calls = 0                          # Save func for later call
        self.func = func
    def __call__(self, *args, **kwargs):        # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):         # On method fetch
        def wrapper(*args, **kwargs):           # Retain both inst
            return self(instance, *args, **kwargs)
        return wrapper(self, instance)    

"""class wrapper:
    def __init__(self, desc, subj):         # Save both instances
        self.desc = desc                    # Route calls back to decr
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs) # Runs tracer.__call__
"""
@tracer
def spam(a, b, c):                      # spam = tracer(spam)
 #...same as prior...                    # Uses __call__ only
    pass

class Person:
    @tracer
    def giveRaise(self, percent):          # giveRaise = tracer(giverRaise)
        pass
 #...same as prior...                    # Makes giveRaise a descriptor

 #==============================================================

import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start = time.perf_counter()
        result = self.func(*args, **kargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result
@timer
def listcomp(N):
    return [x * 2 for x in range(N)]
@timer
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

if __name__ == '__main__':
    result = listcomp(5)                            # Time for this call, all calls, return value
    listcomp(50000)
    listcomp(500000)
    listcomp(1000000)
    print(result)
    print('allTime = %s' % listcomp.alltime)        # Total time for all listcomp calls
    print('')
    result = mapcall(5)
    mapcall(50000)
    mapcall(500000)
    mapcall(1000000)
    print(result)
    print('allTime = %s' % mapcall.alltime)         # Total time for all mapcall calls
    print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))

#=====================================================================
def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):
            start = time.perf_counter()
            result = self.func(*args, **kargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label,self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer

@timer(label='[CCC]==>')
def listcomp(N):                            # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]        # listcomp(...) triggers Timer.__call__

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

for func in (listcomp, mapcall):
    print('')
    result = func(5)                        # Time for this call, all calls, return value
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s' % func.alltime)        # Total time for all calls

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))

#=========================================================================================

def Tracer(aClass):                                     # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kargs):             # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)       # Use enclosing scope name
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)                 # Catches all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname)      # Delegate to wrapped obj
    return Wrapper
    
@Tracer
class Spam:                                 # Spam = Tracer(Spam)
    def display(self):                      # Spam is rebound to Wrapper
        print('Spam!' * 8)
        
@Tracer
class Person:                               # Person = Tracer(Person)
    def __init__(self, name, hours, rate):  # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):                          # Accesses outside class traced
        return self.hours * self.rate       # In-method accesses not traced
    
food = Spam()                               # Triggers Wrapper()
food.display()                              # Triggers __getattr__
print([food.fetches])

bob = Person('Bob', 40, 50)                 # bob is really a Wrapper
print(bob.name)                             # Wrapper embeds a Person
print(bob.pay())

print('')
sue = Person('Sue', rate=100, hours=60)     # sue is a different Wrapper
print(sue.name)                             # with a different Person
print(sue.pay())

print(bob.name)                             # bob has different state
print(bob.pay())
print([bob.fetches, sue.fetches])           # Wrapper attrs not traced

#=========================================================================

# Registering decorated objects to an API

registry = {}
def register(obj):                  # Both class and func decorator
    registry[obj.__name__] = obj    # Add to registry
    return obj                      # Return obj itself, not a wrapper

@register
def spam(x):
     return(x ** 2)                 # spam = register(spam)

@register
def ham(x):
    return(x ** 3)

@register
class Eggs:                         # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4
    def __str__(self):
        return str(self.data)
    
print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))                                  # Invoke objects manually
print(ham(2))                                   # Later calls not intercepted
X = Eggs(2)
print(X)

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](3))        # Invoke from registry

#=================================================================================

"""
Privacy for attributes fetched from class instances.
See self-test code at end of file for a usage example.
Decorator same as: Doubler = Private('data', 'size')(Doubler).
Private returns onDecorator, onDecorator returns onInstance,
and each onInstance instance embeds a Doubler instance.
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):                                     # privates in enclosing scope
    def onDecorator(aClass):                                # aClass in enclosing scope
        class onInstance:                                   # wrapped in instance attribute
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):                    # My attrs don't call getattr
                trace('get:', attr)                         # Others assumed in wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):                 # Outside accesses
                trace('set:', attr, value)                      # Others run normally
                if attr == 'wrapped':                           # Allow my attrs
                    self.__dict__[attr] = value    #!!!!!!!!!!!!   # Avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)          # Wrapped obj attrs
        return onInstance                                       # Or use __dict__
    return onDecorator

if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')                        # Doubler = Private(...)(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label                      # Accesses inside the subject class
            self.data = start                       # Not intercepted: run normally
        def size(self):
            return len(self.data)                   # Methods run with no checking
        def double(self):                           # Because privacy not inherited
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))

    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])
                        
    # The followng all succeed
    print(X.label)                                  # Accesses outside subject class
    X.display(); X.double(); X.display()            # Intercepted: validated, delegated
    print(Y.label)
    Y.display(); Y.double()
    Y.label = 'Spam'
    Y.display()
    # The following all fail properly
"""
 print(X.size()) # prints "TypeError: private attribute fetch: size"
 print(X.data)
 X.data = [1, 1, 1]
 X.size = lambda S: 0
 print(Y.data)
 print(Y.size())
"""
#======================================================================

"""
Class decorator with Private and Public attribute declarations.
Controls access to attributes stored on an instance, or inherited
by it from its classes. Private declares attribute names that
cannot be fetched or assigned outside the decorated class, and
Public declares all the names that can. Caveat: this works in
3.0 for normally named attributes only: __X__ operator overloading
methods implicitly run for built-in operations do not trigger
either __getattr__ or __getattribute__ in new-style classes.
Add __X__ methods here to intercept and delegate built-ins.
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes)) 

traceMe = True
@Private('age')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
X=Person('Bob', 40)
X.name
X.name = 'sue'
X.name
#X.age
#X.age = 'Tom'

@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
X = Person('bob', 40)
X.name
X.name = 'Sue'
X.name
#X.age
#X.age = 'Tom'

#=============================================================

def rangetest(*argchecks):          # Validate positional arg ranges
    def onDecorator(func):
        if not __debug__:           # True if "python -O main.py args..."
            return func             # No-op: call original directly
        else:                       # Else wrapper while debugging
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator

print(__debug__)                                # False if "python –O main.py"

@rangetest((1, 0, 120))                         # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):                        # age must be in 0..120
    print('%s is %s years old' % (name, age))

@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
    @rangetest([1, 0.0, 1.0])                   # giveRaise = rangetest(...)(giveRaise)
    def giveRaise(self, percent):               # Arg 0 is the self instance here
        self.pay = int(self.pay * (1 + percent))

# Comment lines raise TypeError unless "python -O" used on shell command line

persinfo('Bob Smith', 45)                       # Really runs onCall(...) with state
#persinfo('Bob Smith', 200)                     # Or person if –O cmd line argument

birthday(5, 31, 1963)
#birthday(5, 32, 1963)

sue = Person('Sue Jones', 'dev', 100000)
sue.giveRaise(.10)                              # Really runs onCall(self, .10)
print(sue.pay)                                  # Or giveRaise(self, .10) if –O
#sue.giveRaise(1.10)
#print(sue.pay)

#======================================================================

"""
File devtools.py: function decorator that performs range-test
validation for passed arguments. Arguments are specified by
keyword to the decorator. In the actual call, arguments may
be passed by position or keyword, and defaults may be omitted.
See devtools_test.py for example use cases.
"""

trace = True

def rangetest(**argchecks):             # Validate ranges for both+defaults
    def onDecorator(func):              # onCall remembers func and argchecks
        if not __debug__:               # True if "python –O main.py args..."
            return func                 # Wrap if debugging; else use original
        else:
            import sys
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def onCall(*pargs, **kargs):
                # All pargs match first N expected args by position
                # The rest must be in kargs or be omitted defaults
                positionals = list(allargs)
                positionals = positionals[:len(pargs)]

                for (argname, (low, high)) in argchecks.items():
                    # For all args to be checked
                    if argname in kargs:
                        # Was passed by name
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        # Was passed by position
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                        # Assume not passed: default
                        if trace:
                            print('Argument "{0}" defaulted'.format(argname))
                return func(*pargs, **kargs)            # OK: run original call
            return onCall
    return onDecorator

# Test functions, positional and keyword

@rangetest(age=(0, 120))                # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2009))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)
#persinfo('Bob', 150)
#persinfo(age=150, name='Bob')
#birthday(5, D=40, Y=1963)

# Test methods, positional and keyword

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
                                            # giveRaise = rangetest(...)(giveRaise)
    @rangetest(percent=(0.0, 1.0))          # percent passed by name or position
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

bob = Person('Bob Smith', 'dev', 100000)
sue = Person('Sue Jones', 'dev', 100000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)
#bob.giveRaise(1.10)
#bob.giveRaise(percent=1.20)

# Test omitted defaults: skipped

@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)

omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)

#omitargs(1, 2, 3, 11) # Bad d
#omitargs(1, 2, 11) # Bad c
#omitargs(1, 2, 3, d=11) # Bad d
#omitargs(11, d=4) # Bad a
#omitargs(d=4, a=11) # Bad a
#omitargs(1, b=11, d=4) # Bad b
#omitargs(d=8, c=7, a=11) # Bad a

#====================================================================

"""def typetest(**argchecks):
    def onDecorator(func):
        ....
        def onCall(*pargs, **kargs):
            positionals = list(allargs)[:len(pargs)]
            for (argname, type) in argchecks.items():
                if argname in kargs:
                    if not isinstance(kargs[argname], type):
                        ...
                        raise TypeError(errmsg)
                elif argname in positionals:
                    position = positionals.index(argname)
                    if not isinstance(pargs[position], type):
                        ...
                        raise TypeError(errmsg)

                    else:
                        # Assume not passed: default
                return func(*pargs, **kargs)
            return onCall
    return onDecorator
@typetest(a=int, c=float)
def func(a, b, c, d): # func = typetest(...)(func)
 ...
func(1, 2, 3.0, 4) # Okay
func('spam', 2, 99, 4) # Triggers exception correctly"""