# import os
import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine, engine
from sqlalchemy.sql import text

class final:
    def authenticate(self,user, password):
        config = {'user':user,
                  'password':password,
                  'host':'localhost',
                  'port':3306,
                  'database':'akash'}

        df_user = config['user']
        df_password = config['password']
        df_host = config['host']
        df_port = config['port']
        df_database = config['database']

        engine = create_engine(f'mysql+pymysql://{df_user}:{df_password}@{df_host}:{df_port}/{df_database}')
        with engine.connect() as conn:

            conn.execute('''
            CREATE TABLE IF NOT EXISTS IIITL
            (
                name varchar(40),
                batch varchar(10),
                email varchar(60) NOT NULL UNIQUE,
                phone bigint(10)
            );
            ''')
        return engine

    def submit(self,add_entry,name,batch,phone,email,n,p,e,user,password):
        
        if(len(name)==0 or len(phone)==0 or len(email)==0 or len(batch)==0):
            return

        eng = self.authenticate(user,password)
        with eng.connect() as conn:
            try:
                conn.execute(text(f'Insert Into IIITL(name,batch,email,phone) VALUES("{name}","{batch}","{email}","{phone}")'))
            except:
                ttk.Label(add_entry,text='Email already exists. Try Again').grid(column=1)
                return
        
        n.delete(0,tk.END)
        p.delete(0,tk.END)
        e.delete(0,tk.END)

    def search(self,search,email,user, password):
        eng = self.authenticate(user,password)
        with eng.connect() as conn:
            leng = conn.execute(text('SELECT COUNT(*) from IIITL')).fetchall()
            length = leng[0][0]
            if length == 0:
                ttk.Label(search,text='No students added. Add student first').grid(row=2,column=1)
                return
            
            name = conn.execute(text(f'Select * from IIITL where email="{email}"')).fetchall()
            
            if(len(name)==0):
                ttk.Label(search,text='No Student found with this email id.').grid(column=1)
                return

            studlist = name[0]
            ttk.Label(search,text=f'Name: {studlist[0]}\nBatch: {studlist[1]}\nEmail: {studlist[2]}\nPhone: {studlist[3]}').grid(column=1)
