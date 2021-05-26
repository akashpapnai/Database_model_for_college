import tkinter as tk
from sqlalchemy import create_engine
from main import mainwindow

class check():
  def chk(self,user,password,usrget,pwdget,df_host,df_port,df_database):
    try:
      engine = create_engine(f'mysql+pymysql://{usrget}:{pwdget}@{df_host}:{df_port}/{df_database}')
      engine.connect()
      mainwindow().run(usrget,pwdget)
      
    except:
      user.delete(0,tk.END)
      password.delete(0,tk.END)
      print("ERROR, WRONG CREDENTIALS (PLEASE MAKE SURE THAT MYSQL 3306 PORT NUMBER IS CURRENTLY ACTIVE)")
      print("TRY AGAIN")
      