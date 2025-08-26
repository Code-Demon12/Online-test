from tkinter import *
import random
import time
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import matplotlib as plt

root=Tk()
root.title("Test 2023")
root.geometry("600x1000")
sub=''
count=0
con=sqlite3.connect("data.db")
c=con.cursor()

c.execute('SELECT * FROM paper')
a=c.fetchall()
l=len(a)
con.commit()
con.close()
#Result
def result(count,root):
     root.destroy()
     root=Tk()
     root.title("Test 2023")
     root.geometry("600x1000")
     Label(root,text=str(count)+" out of "+str(l),font=("cooper black",28,"bold")).pack()
     root.mainloop()

    
#checking

def Clicked(r,check):
     global sub,count
     sub=(r.get())
     print(check)
     print(sub)
     if(sub==check):
          count=count+1
     

#next question   
def nexting(i,l,root):
     if(i<l):
          root.destroy()
          root=Tk()
          root.title("Test 2023")
          root.geometry("600x1000")
          Label(root,text="Question "+str(i+1),font=("arial",18)).pack()
          r=StringVar()
          r.set(' ')
     
          q=0
          ans=""
          for j in a[i]:
               if(q==0):
                    q=q+1
                    Label(root,text=j,font=("cooper black",18)).pack()
                    continue
               if(q==5):
                    ans=j
                    continue
               rt=Radiobutton(root,text=j,value=j,variable=r,command=lambda:Clicked(r,ans))
               rt.pack()
               q=q+1
          
          #print(count)
          i=i+1
          Button(root,text="next",command=lambda:nexting(i,l,root)).pack()
     else:
          root.destroy()
          root=Tk()
          root.title("Test 2023")
          root.geometry("600x1000")
          Label(root,text="Question "+str(i+1),font=("arial",18)).pack()
          r=StringVar()
          r.set(' ')
     
          q=0
          ans=""
          for j in a[i]:
               if(q==0):
                    q=q+1
                    Label(root,text=j,font=("cooper black",18)).pack()
                    continue
               if(q==5):
                    ans=j
                    continue
               rt=Radiobutton(root,text=j,value=j,variable=r,command=lambda:Clicked(r,ans))
               rt.pack()
               q=q+1
          Button(root,text="Submit",command=lambda:result(count,root)).pack()
     root.mainloop()

Button(root,text="Start",command=lambda:nexting(0,l-1,root),font=("Algerian",28,"bold")).place(x=200,y=400)
root.mainloop()

