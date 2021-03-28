class Laptop:
    discount_percent = 10
    def __init__(self,brand_name,model_name,price):
        #instance variables
        self.brand = brand_name
        self.model = model_name
        self.prices = price
        self.laptop_name = brand_name + ' ' +model_name
        
    def apply_discount(self):
        cut_off = (self.discount_percent/100)*self.prices
        return self.prices - cut_off

# Laptop.discount_percent = 0      
laptop3 = Laptop('hp', 'aul14tx', 63000)
laptop4 = Laptop('Apple', 'macbook pro', 220000)
laptop4.discount_percent = 50
print(laptop4.__dict__)
print(laptop4.apply_discount())
 