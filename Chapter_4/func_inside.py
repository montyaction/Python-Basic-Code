def greater(a,b):
    if a > b:
        return a
    else:
        return b

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c


# def new_greatest(a,b,c):
#     bigger = greater(a,b)
#     return greater(bigger,c)

def new_greatest(a,b,c):
    return greater(greater(a,b),c)

num1 = int(input("Enter fist number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
print(new_greatest(num1,num2,num3))
