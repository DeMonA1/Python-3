class Spam: 
    numInstances = 0
    def __init__(Self):
        Spam.numInstances += 1
    
    def printNumInstances():
        print('Number if instances created: %s' % Spam.numInstances)
    
    printNumInstances = staticmethod(printNumInstances)

"""a = Spam()
b = Spam()
Spam.printNumInstances()
a.printNumInstances()"""

class Sub(Spam):
    def printNuminstances():
        print('Extra stuff...')
        Spam.printNumInstances()
    printNuminstances = staticmethod(printNuminstances)
