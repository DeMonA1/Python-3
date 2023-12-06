class ListInstance:
    """
    Подмешиваемый класс, который предоставляет форматированную функцию
print() или str () для экземпляров через наследование реализованного
в нем метода __str__ ; отображает только атрибуты экземпляра; self
является экземпляром самого нижнего класса;
имена __X предотвращают конфликты c атрибутами клиента
    """
    
    def __atrrnames(self):
        return ''.join('\t%s=%s\n' % (attr, self.__dict__[attr])
                   for attr in sorted(self.__dict__))
    
    def __str__(self):
        return '<Instance of %s%s, address %s:\n%s>' % (
            self.__class__.__name__,            # Имя класса
            tuple(i.__name__ for i in self.__class__.__bases__),
            id(self),                           # Адрес
            self.__atrrnames())                 # Список имя=значение

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInstance)