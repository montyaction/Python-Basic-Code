# can we derive more than one class from base class ?
# multilevel inheritance
# method resolution order
# method overriding
# isinstance(), issubclass()

class Phone:    # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}..."

class Samrtphone(Phone):    # derived / chid class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)    # uncommon way

        super().__init__(brand, model_name, price)
        self.ram =ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


class Samrtphone2(Phone):    # derived / chid class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)    # uncommon way

        super().__init__(brand, model_name, price)
        self.ram =ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
        

smartphone = Samrtphone2('Sony Xperia', '1', 50000, '6GB', '128GB', '20 MP')
# print(phone.full_name())
print(smartphone.full_name() + f"and price is {smartphone._price}")
print(smartphone.full_name())