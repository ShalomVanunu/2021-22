from tkinter import *

app = Tk()
app.title("My New App")
app.geometry("500x500")
app.iconbitmap('Minion.ico')
app.resizable(False,False)


label1 = Label(app, text="Cyber Security",font=('Arial Bold',50))
label1.grid(column=1 , row=0)
Entry = Entry(app, width=10)
Entry.focus()
Entry.grid(column=1 , row=4)
def clicked():
    # The first part, "1.0" means that the input should be read from line one to the END
    messageWindow.delete(1.0, END)
    messageWindow.insert(END,Entry.get())
Btn = Button(app, text="Covid 19",command=clicked)
Btn.grid(column=1 , row=3)

messageWindow = Text(app ,width="20", height="4")
messageWindow.grid(column=1 , row=6)

app.mainloop()

