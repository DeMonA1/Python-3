class Methods:
    def imeth(self, x):     # Nормальный метод экземпляра: передается self
        print([self, x])
    
    def smeth(x):           #  Статический метод: экземпляр не передается
        print([x])
    
    def cmeth(cls, x):      #  Метод класса: получает класс, а не экземпляр
        print([cls,x])
    @property
    def name(self):
        return 'Bob' + self.__class__.__name__
    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)

obj = Methods()
obj.smeth(1)
Methods.smeth(1)

obj.cmeth(3)
Methods.cmeth(5)

print(obj.name)