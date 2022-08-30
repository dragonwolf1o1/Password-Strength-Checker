from tkinter import *
import hashlib
import re
from tkinter import messagebox

myGui = Tk()
myGui.geometry('550x350+700+250')
myGui.title('Checker')
guiFont = font = dict(family='Courier New, monospaced', size=18)
myGui.config(bg='#1F45FC')

eLabel = Label(myGui, text="Please Enter your Password", font=guiFont,bg='#BDEDFF').place(x=150,y=10)
code = StringVar()
ePassword = Entry(myGui,textvariable=code, show="*",font="Robote 20")
ePassword.place(x=180,y=80,height=40,width=200)

#Check Strength

def checkStrength():
    password=code.get()
    if password == "":
        messagebox.showerror("encryption", "Input Password")

    else:
        strength = ['Password can not be Blank', 'Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong']
        score = 1
        password = ePassword.get()

        if len(password) < 1:
            return strength[0]

        if len(password) < 4:
            return strength[1]

        if len(password) >= 8:
            score += 1

        if re.search("[0-9]", password):
            score += 1

        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            score += 1

        if re.search(".", password):
            score += 1

        passwordStrength.set(strength[score])
passwordStrength = StringVar()
checkStrBtn = Button(myGui, text="Check Strength", command=checkStrength, height=2, width=25, font=guiFont,bg='#BDEDFF').place(x=10,y=160,height=60,width=200)
checkStrLab = Label(myGui, textvariable=passwordStrength)
checkStrLab.place(x=250,y=170,height=30,width=150)
checkStrLab.config(bg='#BDEDFF')

#Hashing

def passwordHash():
    hash_obj1 = hashlib.md5()
    pwmd5 = ePassword.get().encode('utf-8')
    hash_obj1.update(pwmd5)
    md5pw.set(hash_obj1.hexdigest())

md5pw = StringVar()
hashBtn = Button(myGui, text="Generate Hash", command=passwordHash, height=2, width=25, font=guiFont,bg='#BDEDFF')
hashBtn.place(x=10,y=240,width=200,height=60)
hashLbl = Label(myGui, textvariable=md5pw)
hashLbl.place(x=250,y=255,height=30,width=250)
hashLbl.config(bg='#BDEDFF')


myGui.mainloop()