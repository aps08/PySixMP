import Constants as C
from file_operation import FileOperations

class PasswordManager:
    def __init__(self) -> None:
        self.root = C.Tk()
        self.File_ops = FileOperations()
        self.root.title(C.TITLE)
        self.root.resizable(False, False)
        self.root.config(padx=20, pady=20, bg=C.BG_COLOR)
        self.main_canvas = C.Canvas(height=200, width=200, bg=C.BG_COLOR, highlightthickness=0)
        self.logo = C.PhotoImage(file=C.LOGO_PATH)
        self.main_canvas.create_image(100, 100, image=self.logo)
        self.main_canvas.grid(column=1, row=1)
        self.labels()
        self.entries()
        self.buttons()
        self.root.mainloop()
        
    def labels(self) -> None:
        self.website_link = C.Label(text="Website Link", font=C.FONT, bg=C.BG_COLOR,highlightthickness=0).grid(column=0, row=2)
        self.email = C.Label(text="Email", font=C.FONT, bg=C.BG_COLOR, highlightthickness=0).grid(column=0, row=3)
        self.Password = C.Label(text="Password", font=C.FONT, bg=C.BG_COLOR, highlightthickness=0).grid(column=0, row=4)

    def entries(self) -> None:
        self.website_entry = C.Entry(width=35, border=3, font=C.FONT)
        self.website_entry.grid(column=1, row=2, columnspan=2)
        self.website_entry.focus()
        self.email_entry = C.Entry(width=35, border=3, font=C.FONT)
        self.email_entry.grid(column=1, row=3, columnspan=2)
        self.email_entry.insert(0, C.DEFAULT_EMAIL)
        self.password_entry = C.Entry(width=35, border=3, font=C.FONT)
        self.password_entry.grid(column=1, row=4, columnspan=2)

    def buttons(self) -> None:
        self.generate_password_btn = C.Button(text="Generate",border=3,command= self.generate_pass, font=C.FONT, width=25, activeforeground="red", fg="red", bg = "light blue", relief = "groove").grid(column=3, row=4)
        self.reset_btn = C.Button(text="Reset",border=3,command= self.reset_data, font=C.FONT, width=25, fg="red",activeforeground="red", bg = "light blue", relief = "groove").grid(column=3, row=5)
        self.get_pass_btn = C.Button(text="Get Password",border=3,command= self.get_data, font=C.FONT, width=25,activeforeground="red", fg="red", bg = "light blue", relief = "groove").grid(column=3, row=2)
        self.add_btn = C.Button(text="Add to Password Manager", command= self.save_data, border=3, font=C.FONT,activeforeground="red", width=30, fg="red",  bg = "light blue", relief = "groove").grid(column=1, row=5, columnspan=2)
        self.exit_btn = C.Button(text="Exit", command= self.exit_program, border=3, font=C.FONT,activeforeground="red", width=30, fg="red",  bg = "light blue", relief = "groove").grid(column=1, row=6, columnspan=2)

    def validate_input(self, domain: str, email: str) -> bool and str:
        if C.validators.domain(domain):
            if C.validators.email(email):
                return True,""
            else:
                return False, C.EMAIL_ERROR
        else:
            return False, C.DOMAIN_ERROR

    def save_data(self) -> None:
        check_ok, message = self.validate_input(self.website_entry.get(), self.email_entry.get())
        if check_ok:
            confirmation = C.messagebox.askyesno(title="Confirmation", message=f"Are you sure ?\nwebsite: {self.website_entry.get()}\nEmail: {self.email_entry.get()}\nPassword: {self.password_entry.get()}")
            if confirmation:
                result = self.File_ops.save_data( self.website_entry.get(), self.email_entry.get(), self.password_entry.get())
                if not result:
                    C.messagebox.showerror(title="Error", message=C.DOMAIN_EXISTS_ERROR)
                else:
                        self.website_entry.delete(0, C.END)
                        self.password_entry.delete(0, C.END)
                        C.messagebox.showinfo(title="Success", message=C.SAVE_SUCCESS)
        else:
            C.messagebox.showerror(title="Error", message=message)
            

    def reset_data(self) -> None:
        self.website_entry.delete(0, C.END)
        self.password_entry.delete(0, C.END)

    def get_data(self) -> None:
        check_ok, message = self.validate_input(self.website_entry.get(), self.email_entry.get())
        if check_ok:
            data_exists, email, password = self.File_ops.search_data(self.website_entry.get())
            if data_exists:
                self.email_entry.delete(0, C.END)
                self.password_entry.delete(0, C.END)
                self.email_entry.insert(0, email)
                self.password_entry.insert(0, password)
                C.messagebox.showinfo(title="Success", message=C.SUCCESS_GET)
            else:
                C.messagebox.showerror(title="Error", message=C.NO_DATA)
        else:
            C.messagebox.showerror(title="Error", message=message)

    def generate_pass(self) -> None:
        self.password_entry.delete(0, C.END)
        length_of_password = 0
        while length_of_password <= 8 & length_of_password <= 25:
            length_of_password = C.simpledialog.askinteger(title="Integer", prompt="Enter length of password", parent=self.root)
            if length_of_password < 8 and length_of_password >25:
                C.messagebox.showinfo(title="Info", message=C.LENGTH_ERROR)
        generated = ''.join([C.random.choice(C.random.choice(C.LIST)) for _ in range(length_of_password)])
        self.password_entry.insert(0, generated)
        C.pyperclip.copy(generated)
        C.messagebox.showinfo(title="Info", message=C.PASSWORD_COPY)

    def exit_program(self)->None:
        print("Closing....")
        C.sys.exit()
        
if __name__ == "__main__":
    print("Running..")
    PM = PasswordManager()