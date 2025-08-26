from tkinter import *
import random
import time
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Test 2023")
root.geometry("600x1000")

#Create Database
#con=sqlite3.connect("data.db")
#c=con.cursor()
#c.execute('''CREATE TABLE paper (
#que text,o1 text,o2 text,o3 text,o4 text,ans text)''')
#con.commit()
#con.close()
con=sqlite3.connect("data.db")
cd=con.cursor()
cd.execute('SELECT * FROM paper')
lis=cd.fetchall()
l=len(lis)
con.commit()
con.close()
def add():
     global a,b,c,d,e,que
     if(len(a.get())!=0 and len(b.get())!=0 and len(c.get())!=0 and len(d.get())!=0 and len(e.get())!=0 and len(que.get())!=0):
          con=sqlite3.connect("data.db")
          cd=con.cursor()
          cd.execute('INSERT INTO paper VALUES(:que,:o1,:o2,:o3,:o4,:ans)',
                    {
                         'que' : que.get(),
                         'o1' : a.get(),
                         'o2' : b.get(),
                         'o3' : c.get(),
                         'o4' : d.get(),
                         'ans' : e.get()
                    }
                    )
          con.commit()
          con.close()
          que.delete(0,END)
          a.delete(0,END)
          b.delete(0,END)
          c.delete(0,END)
          d.delete(0,END)
          e.delete(0,END)
          print("Question Added")
     else:
          messagebox.showerror("Error","Fill all the information")
     
                    
def remove(root,lis,l):
    root.destroy()
    root=Tk()
    root.title("Test 2023")
    root.geometry("600x1000")
    for i in range(l):
        q=0
        for j in lis[i]:
             if(q==0):
                  q=q+1
                  Label(root,text=j,font=("cooper black",18)).place(x=25,y=i*60+10)
                  continue
             if(q==5):
                  continue
      
     
Label(root,text="Question",font=("arial",18)).place(x=25,y=10)
Label(root,text="Option 1",font=("arial",18)).place(x=25,y=70)
Label(root,text="Option 2",font=("arial",18)).place(x=25,y=130)
Label(root,text="Option 3",font=("arial",18)).place(x=25,y=190)
Label(root,text="Option 4",font=("arial",18)).place(x=25,y=250)
Label(root,text="Answer",font=("arial",18)).place(x=25,y=310)
que=Entry(root,width=100,font=("arial",18))
que.place(x=150,y=10)

a=Entry(root,width=30,font=("arial",18))
a.place(x=150,y=70)
b=Entry(root,width=30,font=("arial",18))
b.place(x=150,y=130)
c=Entry(root,width=30,font=("arial",18))
c.place(x=150,y=190)
d=Entry(root,width=30,font=("arial",18))
d.place(x=150,y=250)
e=Entry(root,width=30,font=("arial",18))
e.place(x=150,y=310)

Button(root ,text=" add ",command=lambda:add(),cursor="hand2",font=("cooper black",16,"bold"),bd=5,fg="white",bg="black").place(x=180,y=400)
Button(root ,text=" remove ",command=lambda:remove(root,lis,l),cursor="hand2",font=("cooper black",16,"bold"),bd=5,fg="white",bg="black").place(x=180,y=500)   
root.mainloop()


