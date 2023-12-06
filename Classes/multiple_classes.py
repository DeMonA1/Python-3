# реализация подмешиваемых классов отображения
class Spam:
    def __init__(self):     # метод __repr__ or __str__ отсутствует
        self.data1 = 'food'
X = Spam()
"""print(X)"""

# Вывод списка атрибутов экземпляра с помощью__ dict__
from listinstance import ListInstance
class Spam(ListInstance): # Наследует метод __str__
    def __init__(self):
        self.data1 = 'food'
x = Spam()
"""print(x)  """          # print() and str() launch __str__
display = str(x)    # вывести строку для интерпретации управляющих символов
display
x               # метод __repr__ по-прежнему использует стандартный формат
