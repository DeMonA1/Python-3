# 1
from typing import Any


class Adder:
    def __init__(self,data):
        self.data = data
    
    def __add__(self, x):
        return Adder(self.data + x)

    def add(self, x, y):
        print('Not Implemented')

class ListAdder(Adder):
    def add(self, x, y):
        sum = x + y
        self.data = sum
        return print(sum) 
    
class DictAdder(Adder):
    def add(self, x, y):
        d = {}
        d[x] = y
        self.data = d
        return print(d)
r = ListAdder(2)
f = ListAdder(1)
c = r + 8


# 2
class MyList():
    def __init__(self, list):
        self.lis = list
    
    def __repr__(self):
        return str(self.lis)

    def __add__(self, x):
        return MyList(self.lis + x)
    
    def __radd__(self, x):
        return MyList(x + self.lis)
    
    
    def __getitem__(self, i):
        return self.lis[i]
    
    def __iter__(self):
        for i in self.lis:
            yield i
    
    def append(self, i):
        return self.lis.append(i)
    
    def sort(self):
        return self.lis.sort()

    def __getattr__(self, name):
        return getattr(self.lis, name)


"""li = [3,1,2]
x = MyList(li)
o = [1,2] + x
class My:
    def __init__(self):
        self.data = [1,2,3,4]
l = My()
l.data.append('s')
print(l.data)"""
#3
class MyListSub(MyList):
    def __init__(self,lis):
        self.count_add = 0
        return MyList.__init__(self,lis)
        
    def __add__(self, x):
        self.count_add +=1
        print(self.count_add)
        return MyList(self.lis + x)      

i = MyListSub([1,2,3])
k = MyListSub([3,4,6,7])
"""i + k 
i + k 
i + k 
i + [3]"""



#4   
class Attrs:
    def __setattr__(self, _name: str, value: Any) -> None:
        print('%s = %s' % (_name, value))
        return object.__setattr__(self, _name, value)
    
    def __getattribute__(self, name: str) -> Any:  # not working
        print(name, object.__getattribute__(self, name))
        return object.__getattribute__(self, name)
    
"""I = Attrs()
I.a = [1,23,45,1213]
I.a + [2]"""

#5
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
    def __and__(self, *other): return self.intersect(*other)    # self & other
    def __or__(self, other): return self.union(other)         # self | other
    def __repr__(self): return 'Set:' + repr(self.data)       # print(self),...
    def __iter__(self): return iter(self.data)                # for x in self, ...

class Set1(Set):

    def union(self, *args):             # other - любая последовательность
        res = self.data[:]              # Копировать список
        for x in range(len(args)):
            for i in args[x]:                 # Добавить элементы в other
                if not x in res:
                    res.append(i)
        return Set(res)
    
    def intersect(self, *args):         # other - любая последовательность
        res = []                        # self = подчинённый объект
        for x in self.data:
            for j in range(len(args)):
                for i in args[j]:                 # Добавить элементы в other
                    if x in i:
                        res.append(i)
        return Set(res)     
    def __and__(self, *other): return self.intersect(*other)    # self & other
    
p =Set1('asd')
c = Set1('sad')
b = Set1('asdvxn')
"""o = p & b & c"""
"""print(o)"""

# 7
class Lunch:
    def __init__ (self): # Создает/внедряет экземпляры Customer и Employee
        self.customer = Customer()
        self.employee = Employee()

    def order (self, foodName): # Начинает эмуляцию заказа экземпляром Customer
        return self.customer.placeOrder(foodName, self.employee)
    
    def result (self): # Запрашивает у Customer, какой экземпляр Food он имеет
        return self.customer.printFood()
    
class Customer:
    def __init__ (self): # Инициализирует блюдо значением None
        self.foodname = None

    def placeOrder(self, foodName, employee): # Размещает заказ с экземпляром Employee
        self.foodname = foodName
        return employee.takeOrder(foodName)

    def printFood(self): # Выводит название блюда
        print(self.foodname)

class Employee:
    def takeOrder(self, foodName): # Возвращает экземпляр Food с запрошенным названием
        return Food(foodName)                            

class Food:
    def __init__ (self, name): # Сохраняет название блюда  
        self.foodname = name

i = Lunch()
i.order('pizza')
i.result()

# 8

class Animal:
    def reply(self):
        return self.speak()

class Mammal(Animal):
    def speak(self):
        print('Hi!')

class Cat(Mammal):
    def speak(self):
        print('Meow!')

class Dog(Mammal):
    def speak(self):
        print('Gaf')


class Primate(Mammal):
    def speak(self):
        print('!')


class Hacker(Primate):
    pass

spot = Hacker()
spot.reply()


# 9 
class Scene:
    def __init__(self):
        self.customer = Custome()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line(), self.clerk.line(), self.parrot.line()

class Custome:
    def line(self):
        print('customer:"thats one ex-bird!"')

class Clerk:
    def line(self):
        print('clerk: "no its is\'n"')

class Parrot:
    def line(self):
        print('None')

Scene().action()
