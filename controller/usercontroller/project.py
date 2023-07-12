from tkinter import *

def getVals():
    print("Accepted")

root = Tk()
root.geometry("500x300")

Label(root, text="Pyla Registration Form", font="arial 15 bold").grid(row=0, column=2)

name = Label(root, text="Name")
email = Label(root, text="Email ID")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
pannumber = Label(root, text="Pan Number")

name.grid(row=1, column=1)
email.grid(row=2, column=1)
phone.grid(row=3, column=1)
gender.grid(row=4, column=1)
pannumber.grid(row=5, column=1)

nameText = Entry(root, textvariable=StringVar)
emailText = Entry(root, textvariable=StringVar)
phoneText = Entry(root, textvariable=StringVar)
genderText = Entry(root, textvariable=StringVar)
panNumberText = Entry(root, textvariable=StringVar)

nameText = nameText.grid(row=1, column=2)
emailText = emailText.grid(row=2, column=2)
phoneText = phoneText.grid(row=3, column=2)
genderText = genderText.grid(row=4, column=2)
panNumberText = panNumberText.grid(row=5, column=2)

# Submit Button
Button(text="Submit", command=getVals).grid( row=7, column=2)

root.mainloop()

