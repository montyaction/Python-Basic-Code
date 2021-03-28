# instance methods
l = [1,2,3]
l.pop()

class Person:
    def __init__( self, first_name, last_name, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        # if self.age>18:
            # return True 
        return self.age>18


p1 = Person('Archana', 'Kanwar', 26)
p2 = Person('Mohit', 'Kanwar', 27)
print(p1.full_name())
print(p1.is_above_18())
# print(p2.full_name())

print(Person.full_name(p2))


l = [1,2,3]
# clear, pop
# l.clear()
list.clear(l)
print(l)

l2 = [4,5,6]
# l2.append(10)
list.append(l2,10)
print(l2)

