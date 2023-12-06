import shelve
from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 10000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()