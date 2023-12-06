class Set(list):
    def __init__(self, value = []):   # Конструктор
       list.__init__(self)            # Настраивает список
       self.concat(value)           # Копирует изменяемые стандартные значения

    def intersect(self, other):         # other - любая последовательность
        res = []                    
        for x in self:                  # self - подчинённый объект
            if x in other:              # Выбрать общие элементы
                res.append(x)
        return Set(res)                 # Возвратить новый объект Set
    
    def union(self, other):             # other - любая последовательность
        res = Set(self)                 # Копировать текущий и другой список
        res.concat(other)
        return res
    
    def concat(self, value):            # value: list, Set, etc.
        for x in value:                 # delete of dublicates
            if not x in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)

    def __or__(self, other): return self.union(other)
    
    def __repr__(self): return 'Set:' + list.__repr__(self)

if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print(x,y,len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)