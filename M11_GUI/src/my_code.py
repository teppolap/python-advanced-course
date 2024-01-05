
from tkinter import *
#Your code here!


def on_button_press():
    lbl.config(text='Button pressed!')
    
root = Tk()
root.geometry('150x100')

lbl = Label(root, text='Button not pressed!')
lbl.pack(pady=20)

btn = Button(root, text='Press me', command=on_button_press,)
btn.pack()

#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()
