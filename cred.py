from tkinter import ttk
import tkinter as tk
import os
from checkcred import check

first = tk.Tk()

# Define main window
path = os.getcwd()
first.title('Enter your Credentials')
first.iconphoto(True, tk.PhotoImage(file=os.path.join(path,'icon.png')))
first.geometry('400x300')
first.resizable(False,False)

# username, password entry widget for credentials
ttk.Label(first,text='User       ').grid(row=0,column=0)
userstr = tk.StringVar(first)
user = ttk.Entry(first,textvariable=userstr)
user.grid(row=0,column=1,ipady=5,ipadx=50)

ttk.Label(first,text='Password    ').grid(row=1,column=0)
passwordstr = tk.StringVar(first)
password = ttk.Entry(first,textvariable=passwordstr)
password.grid(row=1,column=1,ipady=5,ipadx=50)

df_host,df_port,df_database = 'localhost',3306,'akash'

add = tk.Button(first,text='Enter the database',command=lambda:check().chk(user,password,userstr.get(),passwordstr.get(),df_host,df_port,df_database))
add.grid(column=1)

first.mainloop()