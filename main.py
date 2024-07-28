import tkinter as tk
from errno import errorcode
from tkinter import messagebox as mb

import customtkinter as ctk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database=""
)
cursor = db.cursor()
root = ctk.CTk()
root.geometry("400x400")
root.title("Password Hashed")
windows_width = root.winfo_screenwidth()/2
windows_height = root.winfo_screenheight()/2
width = 300
height = 350
root.geometry(f"{width}x{height}+{int(windows_width-width/2)}+{int(windows_height-height/2)}")
#inner

def passChecker():
    passwd = password.get()
    conpass = confirmPass.get()
    if passwd == conpass:
        validator()
    else:
        print("error")

def validator():
   try:
       newusername = username.get()
       newemail = email.get()
       confirmpass = password.get()
       q = f'INSERT INTO student (name,email,password) VALUES ("{newusername}","{newemail}","{confirmpass}")'
       print(q)
       cursor.execute(q)
       db.commit()
       mb.showinfo("Information", "User Created  successfully")
       username.destroy()
       email.destroy()
       password.destroy()
       root.destroy()
   except mysql.connector.Error as err:
       mb.showinfo("Error", "Database Error")

label = ctk.CTkLabel(root,text="Register",font=("Arial",20),)
label.pack(pady=10)

username = ctk.CTkEntry(root,width=200,placeholder_text="Username")
username.pack(pady=10)

email = ctk.CTkEntry(root,width=200,placeholder_text="Email")
email.pack(pady=10)

password = ctk.CTkEntry(root,width=200,placeholder_text="Password")
password.pack(pady=10)

confirmPass = ctk.CTkEntry(root,width=200,placeholder_text="Confirm Password")
confirmPass.pack(pady=10)

register = ctk.CTkButton(root,text="Register",width=200,command=passChecker)
register.pack(pady=10)


root.resizable(False, False)
root.mainloop()

