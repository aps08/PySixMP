from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk

def save_data():
    pass

def reset_data():
    pass

def get_data():
    pass


FONT = ("Veradana", 8, "bold")

root = Tk()
root.title("Password Manager! 🔓🔓🔓")
root.resizable(False, False)
root.config(padx=20, pady=20, bg="lightgrey")
main_canvas = Canvas(height=200, width=200, bg="lightgrey", highlightthickness=0)
logo = PhotoImage(file="Password_Manager\_assets\logo.png")
main_canvas.create_image(100, 100, image=logo)
main_canvas.grid(column=1, row=1)

website_link = Label(text="Website Link", font=FONT, bg="lightgrey",highlightthickness=0).grid(column=0, row=2)
username_email = Label(text="Username/Email", font=FONT, bg="lightgrey", highlightthickness=0).grid(column=0, row=3)
Password = Label(text="Password", font=FONT, bg="lightgrey", highlightthickness=0).grid(column=0, row=4)

website_entry = Entry(width=35, font=FONT)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()
username_email_entry = Entry(width=35, font=FONT)
username_email_entry.grid(column=1, row=3, columnspan=2)
username_email_entry.insert(0, "defaultemail@gmail.com")
password_entry = Entry(width=35, font=FONT).grid(column=1, row=4, columnspan=2)

generate_password_btn = Button(text="Generate", font=FONT, width=25, fg="red", bg = "light blue", relief = "groove").grid(column=3, row=4)
reset_btn = Button(text="Reset", font=FONT, width=25, fg="red", bg = "light blue", relief = "groove").grid(column=3, row=5)
get_pass_btn = Button(text="Get Password", font=FONT, width=25, fg="red", bg = "light blue", relief = "groove").grid(column=3, row=2)
add_btn = Button(text="Add to Password Manager", font=FONT, width=30, fg="red",  bg = "light blue", relief = "groove").grid(column=1, row=5, columnspan=2)
aaa = ttk.Combobox(values=["January", "February", "March", "April"])
aaa.grid(column=3, row=6)
aaa.current(2)


root.mainloop()