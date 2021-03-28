# define a function
# input
# nums , iterable(tuple, list) containing number as args

# example
# nums = [1,2,3]
# to_power(3,*args)

# output
# list ----> [1**3,8,27]

# if user didn't pass any args them give a user a message "hey you did't pass"
# args

# else
# return list

# NOTE - USE list comprehension


#-----------------***----------SOLUTION----------***---------------#

# l = [1,2,3]

# if l:
    # print("not empty")
# else:
    # print("empty")



def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"

nums = [1,2,4]
print(to_power(2,*nums))


