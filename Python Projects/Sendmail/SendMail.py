import smtplib
connection = smtplib.SMTP('smtp.gmail.com', 465)
connection.ehlo()
connection.starttls()
mypass = '1992@mohit&bhai'
connection.login('mohitkkanwar@gmail.com', mypass)
connection.sendmail("mohitkkanwar@gmail.com','mohitkkanwar@gmail.com','Subject: hello \n\n this is demo message now i tell you real story I'm practices for python program langauge")
connection.quit()