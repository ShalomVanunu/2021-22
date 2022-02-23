
from tkinter import  *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk()

window.title('Import Picture')
window.geometry("500x500")

def openfile():
     global panel
     path= filedialog.askopenfilename(title='open')
     img = Image.open(path)
     img = img.resize((250, 250), Image.ANTIALIAS)
     img = ImageTk.PhotoImage(img)
     panel = Label(window, image=img)
     panel.image = img
     panel.pack()

btn = Button(window, text="load picture",  command = openfile)
btn.pack()

def clear():
   panel.destroy()

btn1 = Button(window, text="clear",  command = clear)
btn1.pack()



window.mainloop()