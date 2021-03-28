# ask user a number like 1256
# caculate sum of digits.....>1+2+5+6

n = (input("Enter a number = "))
total = 0
for i in range(0,len(n)):
    total += int(n[i])
print(total)