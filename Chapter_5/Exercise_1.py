# Define a function which will take list containing as input
# and return list containing square of every elements

# Example
# number = [1,2,3,4,5,6,7,8,9,]
# square_list(numbers)----> return----> [1,4,9,16,25,36,49,64,81]
def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

numbers = list(range(1,11))
print(square_list(numbers))