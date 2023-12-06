class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]
    
    def __iter__(self):
        print('iter=> next:', end='')
        for x in self.data:
            yield x
            print('next:', end='')
    
    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data
X = Iters('spam')
#X[1:]
list(X)