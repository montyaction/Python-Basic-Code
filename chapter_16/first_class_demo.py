# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD, constructor
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT


class Person:
    def __init__(self, first_name, last_name, age):
        # instace variables
        print('Init method // constructor get called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Archana', 'kanwar', 26)
p2 = Person('Mohit', 'kanwar', 27)

print(p1.first_name)
print(p2.first_name)