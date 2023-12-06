def factory(aClass, *args, **kwargs):
    return aClass(*args, **kwargs)
class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

object1 = factory(Spam)
object2 = factory(Person, 'Arthur', 'King')
object3 = factory(Person, name = 'Brian')

print(object1.doit(99))
print(object2.name, object2.job)
print(object3.name, object3.job)
