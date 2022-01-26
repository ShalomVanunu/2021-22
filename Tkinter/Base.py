
from tkinter import *

app = Tk()

app.title("BMI Calc")
app.geometry("500x500")
app.resizable(False,False)

label1 = Label(app, text="BMI Calculator", font=("Arial",20))
label1.pack()
#label1.place(x=40, y=90)

label2 = Label(app, text="Height",bg="black", fg="yellow")
label2.pack()

height_entry = StringVar()
entry1 = Entry(app,width=15, textvariable=height_entry )
entry1.pack()
entry1.focus()

label3 = Label(app, text="Weight",bg="black", fg="yellow")
label3.pack()

weight_entry = StringVar()
entry1 = Entry(app,width=15, textvariable=weight_entry )
entry1.pack()

label_idle = Label(app,font=("Arial",40))
label_idle.pack()

def clickme():
    bmi = float(weight_entry.get())/float(height_entry.get())**2
    bmi = round(bmi,2)
    label_idle.configure(text=bmi)
    text.insert(1.0,str(bmi))


btn1 = Button(app, text="Calc!",command=clickme)
btn1.pack()

text = Text(app, width="25",height="10")
text.pack()


app.mainloop()