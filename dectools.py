import time

# A decorator for both functions and methods

def tracer(func):                   # Use function, not class with __call__
    calls = 0                       # Else "self" is decorator instance only!
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall
def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kargs):
            start = time.perf_counter()
            result = func(*args, **kargs)
            elapsed = time.perf_counter() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label,func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator