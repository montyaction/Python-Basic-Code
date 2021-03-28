str_seconds = int(input("Please enter the number if seconds you wish to convert : "))
hours = str_seconds // 3600
secs_still_remaining = str_seconds % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs = ", hours, "Mins = ", minutes, "Sesc = ", secs_finally_remaining)


n = input("Please enter your age : ")
print(type(n))