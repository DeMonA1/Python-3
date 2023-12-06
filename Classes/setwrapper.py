class Set:
    def __init__(self, value = []):    # Конструктор
        self.data = []
        self.concat(value)              # Управляет списком
    
    def intersect(self, other):         # other - любая последовательность
        res = []                        # self = подчинённый объект
        for x in self.data:
            if x in other:              # Выбрать общие элементы
                res.append(x)
        return Set(res)                 # Возвратить новый объект Set
    
    def union(self, other):             # other - любая последовательность
        res = self.data[:]              # Копировать список
        for x in other:                 # Добавить элементы в other
            if not x in res:
                res.append(x)
        return Set(res)
    
    def concat(self, value):            # value: list, Set...
        for x in value:                 # Delete of dublicates
            if not x in self.data:
                self.data.append(x)
    
    def __str__(self):
        return str(self.data)

    def __len__(self): return len(self.data)  #len(self), if self - True
    def __getitem__(self, key): return self.data[key]   # self[i], self[i:j]
    def __and__(self, other): return self.intersect(other)    # self & other
    def __or__(self, other): return self.union(other)         # self | other
    def __repr__(self): return 'Set:' + repr(self.data)       # print(self),...
    def __iter__(self): return iter(self.data)                # for x in self, ...

s = Set({1,2,3})
c = Set({2,34,5})
u = s | c
print(u)