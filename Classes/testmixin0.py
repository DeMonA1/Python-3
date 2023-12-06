from listinstance import ListInstance       # Получить класс инструмента для вывоа списка атрибутов

class Super:
    def __init__(self):                 # Метод __init__ супрекласса
        self.data1 = 'spam'             # Создать атрибуты экзмепляра
    
    def ham(self):
        pass

class Sub(Super, ListInstance):         # Подмешивание ham and __str__
    def __init__(self):                 # Классы выводящие списки атрибутов, имеют доступ к self
        Super.__init__(self)
        self.data2 = 'eggs'             # Дополнительные атрибуты экземпляра
        self.data3 = 42
    
    def spam(self):                     # Определить здесь ещё один метод
        pass

if __name__ == "__main__":
    X = Sub()
    print(X)