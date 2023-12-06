class ListTree:
    """Подмешиваемый класс, который возвращает в __str__ результат обхода целого
дерева классов и атрибуты всех его объектов, начиная с self и выше;
запускается print () и str() и возвращает сформированную строку;
использует схему именования атрибутов _ X, чтобы избежать конфликтов
имен в клиентах; явно рекурсивно обращается к суперклассам,
для ясности применяет str.format()."""

    def __attrnames(self, obj, indent):
        spaces = " " * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result
    
    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            above = ''.join(self.__listclass(super, indent + 4) for super in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}: \n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),  # Запускается перед форматированием
                above,
                dots)
        
    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here, above
        )
if __name__ == "__main__":
    import testmixin
    testmixin.tester(ListTree)