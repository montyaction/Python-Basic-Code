class Laptop:
    def __init__(self,brand_name,model_name,price):
        #instance variables
        self.brand = brand_name
        self.model = model_name
        self.prices = price
        self.laptop_name = brand_name + ' ' +model_name

    def apply_discount(self, num):
        cut_off = (num/100)*self.prices
        return self.prices - cut_off

laptop1 = Laptop('hp', 'aul14tx', 63000)

laptop2 = Laptop('Apple', 'macbook pro', 220000)

num = int(input('Enter Discount persentage : '))

print(laptop2.apply_discount(num))

#----------NOT_REPEAT_METHOD-----------#

class Laptop2:
    discount_percent = 10
    def __init__(self,brand_name,model_name,price):
        #instance variables
        self.brand = brand_name
        self.model = model_name
        self.prices = price
        self.laptop_name = brand_name + ' ' +model_name
        
    def apply_discount2(self):
        cut_off = (Laptop2.discount_percent/100)*self.prices
        return self.prices - cut_off

laptop3 = Laptop2('hp', 'aul14tx', 63000)

laptop4 = Laptop2('Apple', 'macbook pro', 220000)

print(laptop4.apply_discount2())