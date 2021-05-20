from tkinter import ttk
import tkinter as tk
from final import final

class click:
    def onclick(self,user, password):
        add_entry = tk.Tk()
        add_entry.title('Enter details of Person')
        add_entry.geometry('500x400')
        add_entry.resizable(False,False)

        ttk.Label(add_entry,text='Name       ').grid(row=0,column=0)
        namestr = tk.StringVar(add_entry)
        name = ttk.Entry(add_entry,textvariable=namestr)
        name.grid(row=0,column=1,ipady=5,ipadx=50)

        ttk.Label(add_entry,text='Phone      ').grid(row=1,column=0)
        phonestr = tk.StringVar(add_entry)
        phone = ttk.Entry(add_entry,textvariable=phonestr)
        phone.grid(row=1,column=1,ipady=5,ipadx=50)

        ttk.Label(add_entry,text='Email      ').grid(row=2,column=0)
        emailstr = tk.StringVar(add_entry)
        email = ttk.Entry(add_entry,textvariable=emailstr)
        email.grid(row=2,column=1,ipady=5,ipadx=50)

        ttk.Label(add_entry,text='Batch      ').grid(row=3,column=0)

        batchstr = tk.StringVar(add_entry)
        batch = ttk.OptionMenu(add_entry,batchstr,*["","B. Tech",'M. Tech',"Phd"])
        batch.grid(row=3,column=1,ipadx=60)

        ttk.Button(add_entry,text='Submit',command=lambda:final().submit(add_entry,namestr.get(),batchstr.get(),phonestr.get(),emailstr.get(),name,phone,email,user,password)).grid(row=5,column=1)

        add_entry.mainloop()

    def search(self,user,password):
        search_entry = tk.Tk()
        search_entry.title('Enter details of Person')
        search_entry.geometry('500x400')
        search_entry.resizable(False,False)

        ttk.Label(search_entry,text='Email      ').grid(row=0,column=0)
        emailstr = tk.StringVar(search_entry)
        email = ttk.Entry(search_entry,textvariable=emailstr)
        email.grid(row=0,column=1,ipady=5,ipadx=50)

        ttk.Button(search_entry,text='Search',command=lambda:final().search(search_entry,emailstr.get(),user,password)).grid(row=1,column=1)