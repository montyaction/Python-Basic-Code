from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "My420@#SQL"
mydatabase = "librery"

con = pymysql.Connect(host="localhost",user="root",password=mypass,database="mydatabase")
cur = con.cursor()

# Enter Tanle Name here
issueTable = "books_issued"
bookTable = "books"

# List To store all Book IDs
allBid = []

def issue():

    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status

    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "SELECT bid FROM "+bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "SELECT STATUS FROM "+bookTable+" WHERE bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'avail':
                status True
            else:
                status False
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")

    