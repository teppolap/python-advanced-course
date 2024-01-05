from tkinter import *
import math

#Your code here!

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        discriminant = b**2 - 4*a*c

        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            label_root1.config(text="{:.2f}".format(root1))
            label_root2.config(text="{:.2f}".format(root2))
        else:
            label_root1.config(text="-")
            label_root2.config(text="-")

    except ValueError:
        label_root1.config(text="-")
        label_root2.config(text="-")


root = Tk()
root.title("Toisen asteen yhtälön ratkaisin")


entry_a = Entry(root, width=10)
entry_a.grid(row=0, column=0, padx=10, pady=5)

entry_b = Entry(root, width=10)
entry_b.grid(row=0, column=1, padx=10, pady=5)

entry_c = Entry(root, width=10)
entry_c.grid(row=0, column=2, padx=10, pady=5)


btn = Button(root, text="Laske juuret", command=solve_quadratic)
btn.grid(row=1, column=1, pady=10)


label_root1 = Label(root, text="-")
label_root1.grid(row=2, column=0, columnspan=3)

label_root2 = Label(root, text="-")
label_root2.grid(row=3, column=0, columnspan=3)


Label(root, text="a").grid(row=0, column=0)
Label(root, text="x^2 +").grid(row=0, column=1)
Label(root, text="x +").grid(row=0, column=2)

#Don't modify lines below
if __name__ == "__main__":
    root.mainloop()
