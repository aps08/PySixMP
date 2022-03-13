from tkinter import *
from tkinter import messagebox, simpledialog
import random

LETTERS = [i for i in 'abcdefghijklmnopqrstuvwxyz']
UPPER_LETTERS = [i for i in 'abcdefghijklmnopqrstuvwxyz'.upper()]
NUMBERS = [i for i in "123456789"]
SYMBOLS = [i for i in "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"]
LIST = [LETTERS, NUMBERS, SYMBOLS, UPPER_LETTERS]
EMAIL_REGEX = ""
WEBSITE_REGEX = ""
PASSWORD_REGEX = ""
FONT = ("Veradana", 8, "bold")

def save_data():
    web = website_entry.get()
    email = username_email_entry.get()
    password = password_entry.get()
    confirmation = messagebox.askyesno(title="Confirmation", message=f"Are you sure ? you want to add\nwebsite: {web}\nEmail/Username: {email}\nPassword: {password}")
    if confirmation:
        with open(r"Password_Manager\_assets\user_data.txt", mode="a", encoding="utf-8") as f:
            f.write(f'{web} | {email} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def reset_data():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def get_data():
    pass

def generate_pass():
    password_entry.delete(0, END)
    length_of_password = 0
    while length_of_password<8:
        length_of_password = simpledialog.askinteger(title="Nummber", prompt="Enter length of password", parent=root)
        if length_of_password < 8:
            messagebox.showinfo(title="Info", message="Number must be greater than 8.")
    generated = ''.join([random.choice(random.choice(LIST)) for _ in range(length_of_password)])
    password_entry.insert(0, generated)


root = Tk()
root.title("Password Manager! 🔓🔓🔓")
root.resizable(False, False)
root.config(padx=20, pady=20, bg="lightgrey")
main_canvas = Canvas(height=200, width=200, bg="lightgrey", highlightthickness=0)
logo = PhotoImage(file=r"Password_Manager\_assets\logo.png")
main_canvas.create_image(100, 100, image=logo)
main_canvas.grid(column=1, row=1)

website_link = Label(text="Website Link", font=FONT, bg="lightgrey",highlightthickness=0).grid(column=0, row=2)
username_email = Label(text="Username/Email", font=FONT, bg="lightgrey", highlightthickness=0).grid(column=0, row=3)
Password = Label(text="Password", font=FONT, bg="lightgrey", highlightthickness=0).grid(column=0, row=4)

website_entry = Entry(width=35, border=3, font=FONT)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()
username_email_entry = Entry(width=35, border=3, font=FONT)
username_email_entry.grid(column=1, row=3, columnspan=2)
username_email_entry.insert(0, "defaultemail@gmail.com")
password_entry = Entry(width=35, border=3, font=FONT)
password_entry.grid(column=1, row=4, columnspan=2)

generate_password_btn = Button(text="Generate",border=3,command=generate_pass, font=FONT, width=25, activeforeground="red", fg="red", bg = "light blue", relief = "groove").grid(column=3, row=4)
reset_btn = Button(text="Reset",border=3,command=reset_data, font=FONT, width=25, fg="red",activeforeground="red", bg = "light blue", relief = "groove").grid(column=3, row=5)
get_pass_btn = Button(text="Get Password",border=3, font=FONT, width=25,activeforeground="red", fg="red", bg = "light blue", relief = "groove").grid(column=3, row=2)
add_btn = Button(text="Add to Password Manager", command=save_data, border=3, font=FONT,activeforeground="red", width=30, fg="red",  bg = "light blue", relief = "groove").grid(column=1, row=5, columnspan=2)


root.mainloop()