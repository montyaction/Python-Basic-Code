# print('Enter three number then I will show Total and Average')
# number_one=int(input("Enter first number = "))
# number_two=int(input('Enter second number = '))
# number_three=int(input('Enter third number = '))
# total = number_one+number_two+number_three
# print('Total number is = '+ str(total))
# print('Average number is = '+str(total/3))

# num1 = input("Enter first number = ")
# num2 = input("Enter second number = ")
# num3 = input("Enter third number = ")
# print(f"Total of three number = {(int(num1)+int(num2)+int(num3))}")
# print(f"Average of three number = {(int(num1)+int(num2)+int(num3))/3}")

num1,num2,num3=input('Enter three numbers comma separated = ').split(',')
print(f"Total of three number = {(int(num1)+int(num2)+int(num3))}")
print(f"Average of three number = {(int(num1)+int(num2)+int(num3))/3}")
