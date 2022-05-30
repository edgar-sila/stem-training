# with python
from cProfile import label
from tkinter import *
root =Tk()
#create a frame
edgar= Label (root,text="Hello world")
edgar2=Label (root,text="hello world")
#show it on screen
edgar.grid(row=0,column=2)
edgar2.grid(row=0,column=0)

edgar.configure(bg ="grey")
root.mainloop()
gui