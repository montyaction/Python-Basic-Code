# Exercise one of three
# sum of natural numbers
# ask a user for natural number(n)
# print total from i to n

# total = 0
# i = 1
# n = int(input("Enter any number = "))
# while i <=n:
#     total += i
#     i += 1
#     print(f"sum is : {total} : {i}")



n = input("Enter a number : ") 
n = int(n)
total = 0
i = 1
while i <= n:
    total += i
    i += 1
    print(total)  
