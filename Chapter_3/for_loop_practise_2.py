# ask user name and count each character

name = input("Enter your name : ")
temp = ""
for i in range(len(name)):
    print(f"{name[i]} : {name.count(name[i])}")
    temp += name[i]