class Phone:    # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}...."

class Smartphone(Phone):    # derived / child class 
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)  # Uncommon way
        
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    
phone = Phone('nokia', '1100', 1000)
Smartphone = Smartphone('Sony Xperia', '1 Mark-II', 100000, '8GB', '128GB', '20 MP')
print(phone.full_name())
print(Smartphone.full_name() + f"and price is {Smartphone._price}")