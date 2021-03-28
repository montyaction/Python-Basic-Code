from tkinter import *
import random, string
import pyperclip

# Initialize Window
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("MontyProject - PASSWORD GENERATOR")

Label(root, text = 'PASSWORD GENERATOR', font ='arial 15 bold').pack()
Label(root, text ='Pass Generator Project', font ='arial 15 bold').pack(side=BOTTOM)

# Select Password Lenght
pass_label = Label(root, text = 'How long should the password be? \n Please tell me in numbers. ',font = 'arial 10 bold').pack()
pass_len = IntVar(),
lenght = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width = 15).pack()

# Functio to Generate Password
pass_str = StringVar()
def Generator():
    password = ' '

    for x in range (0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    
    for y in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

        pass_str.set(password)

Button(root, text = "GENERATE PASSSWORD", command = Generator).pack(pady = 5)

Entry(root, textvariable = pass_str).pack()

# Function to Copy Password
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)


root.mainloop()
