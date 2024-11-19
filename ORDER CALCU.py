from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def Check():
    pword = pass_entry.get()
    if pword == "123welcome":
        for widget in frame.winfo_children():
            if isinstance(widget, (Checkbutton, Radiobutton, Button, Entry, Label, ttk.Combobox)):
                widget.config(state='normal')
    else:
        messagebox.showerror("Invalid Password", "Invalid Password!")

def Clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    one.set(0)
    two.set(0)
    three.set(0)
    rice.set(0)
    drinks.set("")
    bill.config(state=NORMAL)
    bill.delete(0,END)
    bill.config(state=DISABLED)

def Compute():
    meal = 0

    if one.get() == 1:
        meal += 25
    if two.get() == 1:
        meal += 30
    if three.get() == 1:
        meal += 35

    if rice.get() == 1:
        meal += 25

    bill.config(state=NORMAL)
    bill.delete(0, END)
    bill.insert(0, str(meal))
    bill.config(state=DISABLED)

def Close():
    if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
        window.destroy()

window = Tk()
window.title("Order Form")
window.geometry("300x400")

frame = Frame(window)
frame.pack()

order = LabelFrame(frame, bd=1, bg='white')
order.grid(row=0, column=0)

user = Label(frame, text="Username: ")
user.grid(row=0, column=0)

user_entry = Entry(frame, bd=1, bg='white')
user_entry.grid(row=0, column=1)

password = Label(frame, text="Password: ")
password.grid(row=1, column=0)

pass_entry = Entry(frame, bd=1, bg='white', show='*')
pass_entry.grid(row=1, column=1)

ok = Button(frame, text="Ok", command=Check)
ok.grid(row=1, column=2)

order_title = Label(frame, text="Choose Your Order:")
order_title.grid(row=3, column=1)

one = IntVar()
meal_one = Checkbutton(frame, text="Value Meal #1: P25.00", variable=one, onvalue=1, offvalue=0, state='disabled')
meal_one.grid(row=4, column=1)

two = IntVar()
meal_two = Checkbutton(frame, text="Value Meal #2: P30.00", variable=two, onvalue=1, offvalue=0, state='disabled')
meal_two.grid(row=5, column=1)

three = IntVar()
meal_three = Checkbutton(frame, text="Value Meal #3: P35.00", variable=three, onvalue=1, offvalue=0, state='disabled')
meal_three.grid(row=6, column=1)

softdrinks = ["Coke", "Sprite", "Pepsi"]
drinks = ttk.Combobox(frame, values=softdrinks, width=7, state='disabled')
drinks.grid(row=6, column=2)

rice = IntVar()
extra_rice = Radiobutton(frame, text="Extra Rice", variable=rice, value=1, state='disabled')
extra_rice.grid(row=7, column=0)

no_extra_rice = Radiobutton(frame, text="No Extra Rice", variable=rice, value=2, state='disabled')
no_extra_rice.grid(row=7, column=1)

compute = Button(frame, text="Compute", bd=1, command=Compute, state='disabled')
compute.grid(row=7, column=2)

total_bill = Label(frame, text="Total Bill is: ")
total_bill.grid(row=8, column=0)

bill = Entry(frame, bd=1, width=20, state='disabled')
bill.grid(row=8, column=1)

clear = Button(frame, text="Clear", bd=1, command=Clear, state='disabled')
clear.grid(row=9, column=1)

close = Button(frame, text="Close", bd=1, command=Close)
close.grid(row=9, column=2)

for widgets in frame.winfo_children():
    frame.grid_configure(padx=10, pady=15)

window.mainloop()