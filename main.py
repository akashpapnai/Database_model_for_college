import tkinter as tk
import os
from clicked import click

class mainwindow:
  def run(self, user, password):
    root = tk.Tk()

    # Define main window
    path = os.getcwd()
    root.title('Enter your Credentials')
    root.geometry('400x300')
    root.resizable(False,False)

    #content of the main window
    add = tk.Button(root,text='Add a person',command=lambda:click().onclick(user, password))
    add.config(width=25,height=5)
    add.pack()

    search = tk.Button(root,text='Search a person',command=lambda:click().search(user,password))
    search.config(width=25,height=5)
    search.pack()

    root.mainloop()