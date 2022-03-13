from tkinter import *
from tkinter import messagebox, simpledialog
import random
import validators

LETTERS = [i for i in 'abcdefghijklmnopqrstuvwxyz']
UPPER_LETTERS = [i for i in 'abcdefghijklmnopqrstuvwxyz'.upper()]
NUMBERS = [i for i in "123456789"]
SYMBOLS = [i for i in "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"]
LIST = [LETTERS, NUMBERS, SYMBOLS, UPPER_LETTERS]
FONT = ("Veradana", 8, "bold")

def validate_input(domain: str, email: str) -> bool | str:
    if validators.domain(domain):
        if validators.email(email):
            return True,""
        else:
            return False,"Doesn't look like a email. Try again."
    else:
        return False, "Doesn't look like a domain. Try again."

def save_data(web: Entry, email: Entry, pwd: Entry) -> None:
    check_ok, message = validate_input(web.get(), email.get())
    if check_ok:
        confirmation = messagebox.askyesno(title="Confirmation", message=f"Are you sure ? you want to add\nwebsite: {web.get()}\nEmail/email: {email.get()}\nPassword: {pwd.get()}")
        if confirmation:
            with open(r"Password_Manager\_assets\user_data.txt", mode="a", encoding="utf-8") as f:
                f.write(f'{web.get()} | {email.get()} | {pwd.get()}\n')
                web.delete(0, END)
                pwd.delete(0, END)
        return
    else:
        messagebox.showerror(title="Error", message=message)
        return
            

def reset_data(web: Entry, pwd: Entry) -> None:
    web.delete(0, END)
    pwd.delete(0, END)
    return

def get_data(web: Entry, email: Entry, pwd: Entry) -> None:
    check_ok, message = validate_input(web.get(), email.get())
    if check_ok:
        read_password = ""
        with open(r"Password_Manager\_assets\user_data.txt", mode="a", encoding="utf-8") as f:
            content = f.read()
        pwd.delete(0, END)
        pwd.insert(0, read_password)
        return
    else:
        messagebox.showerror(title="Error", message=message)
        return

def generate_pass():
    password_entry.delete(0, END)
    length_of_password = 0
    while length_of_password<8:
        length_of_password = simpledialog.askinteger(title="Integer", prompt="Enter length of password", parent=root)
        if length_of_password < 8:
            messagebox.showinfo(title="Info", message="Number must be greater than 8.")
    generated = ''.join([random.choice(random.choice(LIST)) for _ in range(length_of_password)])
    password_entry.insert(0, generated)
    return


root = Tk()
root.title("Password Manager! 🔓🔓🔓")
root.resizable(False, False)
root.config(padx=20, pady=20, bg="lightgrey")
main_canvas = Canvas(height=200, width=200, bg="lightgrey", highlightthickness=0)
logo = PhotoImage(file=r"Password_Manager\_assets\logo.png")
main_canvas.create_image(100, 100, image=logo)
main_canvas.grid(column=1, row=1)

website_link = Label(text="Website Link", font=FONT, bg="lightgrey",highlightthickness=0).grid(column=0, row=2)
email = Label(text="Email", font=FONT, bg="lightgrey", highlightthickness=0).grid(column=0, row=3)
Password = Label(text="Password", font=FONT, bg="lightgrey", highlightthickness=0).grid(column=0, row=4)

website_entry = Entry(width=35, border=3, font=FONT)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35, border=3, font=FONT)
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, "defaultemail@gmail.com")
password_entry = Entry(width=35, border=3, font=FONT)
password_entry.grid(column=1, row=4, columnspan=2)

generate_password_btn = Button(text="Generate",border=3,command=generate_pass, font=FONT, width=25, activeforeground="red", fg="red", bg = "light blue", relief = "groove").grid(column=3, row=4)
reset_btn = Button(text="Reset",border=3,command= lambda: reset_data(website_entry, password_entry), font=FONT, width=25, fg="red",activeforeground="red", bg = "light blue", relief = "groove").grid(column=3, row=5)
get_pass_btn = Button(text="Get Password",border=3, font=FONT, width=25,activeforeground="red", fg="red", bg = "light blue", relief = "groove").grid(column=3, row=2)
add_btn = Button(text="Add to Password Manager", command= lambda: save_data(website_entry,email_entry, password_entry), border=3, font=FONT,activeforeground="red", width=30, fg="red",  bg = "light blue", relief = "groove").grid(column=1, row=5, columnspan=2)


root.mainloop()