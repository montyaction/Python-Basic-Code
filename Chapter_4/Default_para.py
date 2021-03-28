# defualt parameters

# def user_info(first_name,last_name = 'Unkonw',age):     # aisa nhi kar sakte
#     print(f"Your first name is :{first_name}")          # aisa karne par error aayegi
#     print(f"Your last name is :{last_name}")
#     print(f"Your age is : {age}")

# user_info(' MOhit', 24) 


# def user_info(fisrt_name,last_name,age = None):         # aisa kar sakte hai
#     print(f"Your first name is :{first_name}")
#     print(f"Your last name is :{last_name}")
#     print(f"Your age is : {age}")

# user_info(' MOhit', ' Kanwar') 


# def user_info(first_name,last_name = 'Unkonw',age = None):      # aisa kar sakte hai, 
#     print(f"Your first name is :{first_name}")                  # jab hum ending ko "default" bante hai
#     print(f"Your last name is :{last_name}")                    # to hum sting tak "default" ban skate hain
#     print(f"Your age is : {age}")

# user_info(' MOhit')


def user_info(first_name,last_name = 'Unknow',age = None):       
    print(f"Your first name is :{first_name}")
    print(f"Your last name is :{last_name}")
    print(f"Your age is : {age}")

fist_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
age = input("Enter your age : ")
user_info(fist_name,last_name,age)