# define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number

def even_generator(n):
    for nums in range(1,n+1):
        if nums % 2 == 0:
            yield(nums)

even_nums = even_generator(20)
for num in even_nums:
    print(num)



def even_generator2(n):
    for nums in range(2,n+1,2):
        
            yield(nums)

even_nums = even_generator2(30)
for num in even_nums:
    print(num)