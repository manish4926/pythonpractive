import tkinter.font
from tkinter import *
from PIL import ImageTk

# Functionality

def on_enter(event):
    if(usernameEntry.get()=='Username'):
        usernameEntry.delete(0,END)

def password_enter(event):
    if(passwordEntry.get()=='Password'):
        passwordEntry.delete(0,END)

def login_window():
    print('hello')

def hidePassword():
    openeye.configure(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=showPassword)

def showPassword():
    openeye.configure(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hidePassword)

loginWindow = Tk()
loginWindow.geometry("990x660+100+50")
loginWindow.resizable(0,0)
loginWindow.title('User Registration Page')

font = tkinter.font
helv36 = font.Font(family="Helvetica",size=36,weight="bold")
mcfontd = font.Font(family="Microsoft Yehei UI Light",size=23,weight="bold")
arial = font.Font(family="Arial",size=23,weight="bold")
mcfont = "Microsoft Yehei UI Light"
inputFontSize = 11
inputfont = ("Microsoft Yehei UI Light",23,'bold')
fontWeightBold = 'bold'
fontTextColor = 'firebrick1'
fontBackColor = 'white'


bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(loginWindow, image=bgImage)
# bgLabel.grid(row=0, column=0)
bgLabel.place(x=0,y=0)


heading = Label(loginWindow,
                text="User Registration",
                font=(mcfont, 15, 'bold'),
                bg=fontBackColor,
                fg=fontTextColor)
heading.place(x=605,y=120)

# Design
usernameEntry = Entry(loginWindow, width=27, font=(mcfont,inputFontSize,fontWeightBold),
                      bd=0,fg=fontTextColor)
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', on_enter)
Frame(loginWindow, width=250, height=2, bg=fontTextColor).place(x=580, y=222)


passwordEntry = Entry(loginWindow, width=27, font=(mcfont,inputFontSize,fontWeightBold),
                      bd=0,fg=fontTextColor)
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', password_enter)
Frame(loginWindow, width=250, height=2, bg=fontTextColor).place(x=580, y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton = Button(loginWindow, image=openeye, bd=0, bg=fontBackColor, activebackground=fontBackColor, cursor='hand2',
                   command=hidePassword)
eyeButton.place(x=800, y=255)

# Forget Password
forgetButton = Button(loginWindow, text='Forgot password', bd=0, fg=fontTextColor, activeforeground=fontTextColor, bg=fontBackColor, activebackground=fontBackColor, cursor='hand2',
                   command=hidePassword)
forgetButton.place(x=715, y=295)


# Login Button
loginButton = Button(loginWindow, text='Login', bd=0, fg=fontBackColor, activeforeground=fontBackColor, bg=fontTextColor, activebackground=fontTextColor, cursor='hand2',
                     command=hidePassword,width=34)
loginButton.place(x=580, y=325)

loginWindow.mainloop()
