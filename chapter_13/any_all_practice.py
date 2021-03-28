# any all function
def my_sum(*args):
    # args = () 
    if all([(type(arg) == int or type(arg) == float) for arg in args]):

        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong input"

print(my_sum(1,2,3.7,4,5.5,6,7))