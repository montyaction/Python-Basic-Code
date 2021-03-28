# Problem 
# aks user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print

# ask input in string, i.e don't change string to int
#  example - 1256
# pick string character one by one and change int
# int(example [0] +int(example[1].....go up to len(example)


number = input('enter a number = ')
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)
