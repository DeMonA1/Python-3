class Spam: 
    numInstances = 0
    def __init__(Self):
        Spam.numInstances = Spam.numInstances + 1
    
    def printNumInstances():
        print('Number if instances created: %s' % Spam.numInstances)

class Spam: 
    numInstances = 0
    def __init__(Self):
        Spam.numInstances = Spam.numInstances + 1
    
    def printNumInstances(cls):
        print('Number if instances created: %s' % Spam.numInstances)

    printNumInstances = classmethod(printNumInstances)

class Spam: 
    numInstances = 0
    def __init__(Self):
        Spam.numInstances += 1

    def printNumInstances(cls):
        print('Number if instances created: %s, %s' % (cls.numInstances, cls))

    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNuminstances(cls):
        print('Extra stuff...', cls)
        Spam.printNumInstances()
    printNuminstances = classmethod(printNuminstances)

class Other(Spam): pass