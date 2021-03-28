# ask a user for name
# Example - Archana Kanwar
# print count of each words
name = input("Enter your Name : ")
                                            # output
# name.count("A"), name.count(name[0])        A : 1
# name.count("r"), name.count(name[1])        r : 2
# name.count("c"), name.count(name[2])        A : 1
# name.count("h"), name.count(name[3])        A : 1
# name.count("a"), name.count(name[4])        A : 1
# name.count("n"), name.count(name[5])        A : 1
# name.count(" "), name.count(name[6])        A : 1
# name.count("K"), name.count(name[7])        A : 1
# name.count("w"), name.count(name[8])        A : 1

i = 0
temp_var = " "
while i < len(name):
    print(f"{name[i]} : {name.count(name[i])} ")
    i += 1


