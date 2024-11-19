from tkinter import *
from tkinter import ttk

def Enter():
    first = fn_entry.get()
    last = ln_entry.get()
    ttl = title_combobox.get()
    a = age_num.get()
    n = n_entry.get()
    r = r_status.get()
    tc = tnc_status.get()
    print("Welcome, " + ttl + " " + last)
    print("\n\tDETAILS")
    print("First Name: " + first)
    print("Last Name: " + last)
    print("Age: " + str(a))
    print("Nationality: " + n)
    print("Registration Status: " + r)
    print(tc + " the terms and conditions")
    print("----------------------------------------------------------")

def Clear():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    title_combobox.delete(0, END)
    age_num.delete(0, END)
    n_entry.delete(0, END)

window = Tk()
window.geometry("600x550")
window.title("Data Entry Form")

frame = Frame(window)
frame.pack()

user_info = LabelFrame(frame, text="User Information",
                       font=('Arial', 14, 'bold'))
user_info.grid(row=0, column=0, padx=10, pady=10)

first_name = Label(user_info, text="First Name:", font=('Arial', 11))
first_name.grid(row=0, column=0)

last_name = Label(user_info, text="Last Name:", font=('Arial', 11))
last_name.grid(row=0, column=1)

fn_entry = Entry(user_info)
fn_entry.grid(row=1, column=0)

ln_entry = Entry(user_info)
ln_entry.grid(row=1, column=1)

title = Label(user_info, text="Title", font=('Arial', 11))
title.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info, values=["Mr.", "Ms.", "Mrs.", " "])
title_combobox.grid(row=1, column=2)

age = Label(user_info, text="Age:", font=('Arial', 11))
age.grid(row=2, column=0)

age_num = Spinbox(user_info, from_=18, to=75)
age_num.grid(row=3, column=0)

nationality = Label(user_info, text="Nationality:", font=('Arial', 11))
nationality.grid(row=2, column=1)

n_entry = Entry(user_info)
n_entry.grid(row=3, column=1)

for widget in user_info.winfo_children():
    widget.grid_configure(padx=10, pady=10)

courses = LabelFrame(frame)
courses.grid(row=1, column=0, sticky="news", padx=10, pady=10)

registered = Label(courses, text="Registration Status", font=('Arial', 11))
registered.grid(row=1, column=0)

r_status = StringVar(value=" ")

r_check = Checkbutton(courses, text="Currently Registered", variable=r_status,
                      onvalue="Registered", offvalue="Not Registered")
r_check.grid(row=2, column=0)

completed_course = Label(courses, text="# Completed Course/s")
completed_course.grid(row=1, column=1)

cc_num = Spinbox(courses, from_=0, to=10)
cc_num.grid(row=2, column=1)

sem = Label(courses, text="# Semesters")
sem.grid(row=1, column=2)

sem_num = Spinbox(courses, from_=0, to=10)
sem_num.grid(row=2, column=2)

for widget in courses.winfo_children():
    widget.grid_configure(padx=10, pady=10)

tnc = LabelFrame(frame, text="Terms & Conditions", font=('Arial', 12, 'bold'))
tnc.grid(row=2, column=0,sticky="news", padx=10, pady=10)

tnc_status = StringVar(value=" ")

tnc_check = Checkbutton(tnc, text="I accept the terms and conditions", font=('Arial', 11),
                        variable=tnc_status, onvalue="I accept", offvalue="I do not accept")
tnc_check.grid(row=2, column=0, padx=10, pady=10)

button = Button(frame, text="Enter data", font=('Arial', 14, 'bold'), bg='white', command=Enter)
button.grid(row=3, column=0, sticky="news", padx=10, pady=10)

clear = Button(frame, text="CLEAR", font=('Arial', 14, 'bold'), bg='white', command=Clear)
clear.grid(row=4, column=0, sticky="news", padx=10, pady=10)

window.mainloop()