from tkinter import *

root =Tk ()
def myclick():
    mylabel = Label(root,text="hey you clicked")
    mylabel.pack()
myB=Button (root, text="click me!",command=myclick)
myB.pack()

root.mainloop() 