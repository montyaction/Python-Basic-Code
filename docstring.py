from random import seed
# from random import randint
# seed(7)
# print(randint(0,9),randint(0,9),randint(0,9))

# from random import randrange
# print(randrange(-2,4))

from random import gauss
seed(7)
print(gauss(0,1),gauss(0,1),gauss(0,1))

list=[2,4,3,9,6,2,1,0,7,4,3,5,3,6,8]
from random import choice
seed(7)
print(choice(list),choice(list),choice(list),choice(list),choice(list),choice(list))