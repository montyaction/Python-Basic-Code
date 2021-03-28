class Teacher:
    count_instance = 0
    def __init__(self, first_name, last_name, empoye_code, age):
        Teacher.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.code = empoye_code
        self.age = age
    


p1 = Teacher('Archana', 'Kanwar',1214, 26)
p2 = Teacher('Mohit', 'Kanwar',1215, 28)
p3 = Teacher('Monty', 'Kanwar',1216, 27)
print(Teacher.count_instance)