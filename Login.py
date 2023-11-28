from ConnectDB import create_connection, close_connection, get_cursor
conn = create_connection()
cursor = get_cursor(conn)
from code import interact
from multiprocessing.sharedctypes import Value
import tkinter
import mysql.connector as mysql
from tkinter import messagebox
import os
frm = tkinter.Tk()
frm.geometry("400x250")
frm.title("Login")

def showPasswd():
    if (v1.get() == 1):
        txt_pass.config(show="")
    else:
        txt_pass.config(show="*")

def login():
    user = txt_user.get()
    passwd = txt_pass.get()
    query = "SELECT * FROM user where Usern='"+user+"' AND Userp='"+passwd+"'"
    cursor.execute(query)
    infoData = cursor.fetchone()

    if (infoData == None):
        messagebox.showinfo("Result", "Sorry...your username or password incorrect!")
    else:
        frm.destroy()
        os.system("python Display.py")
    
def cancel():
    frm.destroy()

lb1 = tkinter.Label(frm, text="Username:")
lb1.place(x=50, y=20)
lb1.config(font=('Times New Roman', 14, 'bold'))

lb2 = tkinter.Label(frm, text="Password:")
lb2.place(x=50, y=80)
lb2.config(font=('Times New Roman', 14, 'bold'))

txt_user = tkinter.Entry(frm)
txt_user.place(x=160, y=20)
txt_user.config(font=('Times New Roman', 14))

txt_pass = tkinter.Entry(frm, show="*")
txt_pass.place(x=160, y=80)
txt_pass.config(font=('Times New Roman', 14))

v1 = tkinter.IntVar()
cb_pass = tkinter.Checkbutton(frm, text="Show Password", variable=v1, onvalue=1, offvalue=0, command=showPasswd)
cb_pass.place(x=160, y=120)
cb_pass.config(font=('Times New Roman', 14))

btn_save = tkinter.Button(frm, text="Login", width=10, command=login)
btn_save.place(x=60, y=170)
btn_save.config(font=('Times New Roman', 14))

btn_cancel = tkinter.Button(frm, text="Cancel", width=10, command=cancel)
btn_cancel.place(x=230, y=170)
btn_cancel.config(font=('Times New Roman', 14))
aaaaa
frm.mainloop()
