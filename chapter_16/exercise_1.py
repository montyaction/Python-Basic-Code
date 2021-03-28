# Craete a laptop class with attributes like brand name, model name, price
# Craete two objects/instance of your laptop class

class Laptop:
    def __init__(self,brand_name, model_name,price):
        # instance variables
        self.brand = brand_name
        self.name = model_name
        self.price = price
        self.laptop_name = brand_name + ' ' + model_name

laptop1 = Laptop('hp', 'aul14tx', 63000)
print(laptop1.name)
print(laptop1.price) 

print(laptop1.laptop_name)