class Person:
    count_instance = 0  #  class variable / clss attribute
    def __init__( self, first_name, last_name, age ):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    
    
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class"

    
    @staticmethod
    def hello():
        print('hello, static method called')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18


p1 = Person('Archana', 'Kanwar', 26)
p2 = Person('Mohit', 'Kanwar', 27)

p3 = Person.from_string('Monty,Kanwar,28')

print(p1.first_name)
print(p2.last_name)
print(p2.age)
print(p3.full_name())
print(p1.full_name())
print(Person.full_name(p1))


print(Person.count_instances())
Person.hello()