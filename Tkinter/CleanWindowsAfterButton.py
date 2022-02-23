from tkinter import *

app = Tk()
app.title("My New App")
app.geometry("500x500")
app.resizable(False,False)

def click():
    f1 = Frame()
    f1.place(x=0,y=0, width=500,height=500)
    l1 = Label(f1,text="User")
    l1.pack()
    e1 = Entry(f1,width=15)
    e1.pack()
    e1.focus()
    l2 = Label(f1, text="Password")
    l2.pack()
    e2 = Entry(f1, width=15)
    e2.pack()
    b2 = Button(f1,text="Login")
    b2.pack()


b1 = Button(app, text="Clickme!", command=click)
b1.pack()

app.mainloop()