import constants as C

# Here are some global variables.
reps = 0
my_timer = None

class pomodoro_timer:
    """ This class is responsible for running the promodoro timer.
    """
    def __init__(self) -> None:
        """ __init__() --> This is a constructor which is responsible for showing the interface to the user, and intializes some
                            useful variables.
        """ 
        self.window = C.Tk()
        self.window.title(C.TITLE)
        self.window.resizable(False, False)
        self.window.config(padx=150, pady=75, bg="#A1B57D")
        self.title = C.Label(text="Timer", fg="#DD4A48", bg="#A1B57D", font=(C.FONT_NAME, 36, "bold"))
        self.title.grid(column=1, row=0)
        self.canvas = C.Canvas(width=200, height=224, bg="#A1B57D", highlightthickness=0)
        self.IMG = C.PhotoImage(file=C.PATH)
        self.canvas.create_image(100, 112, image=self.IMG)
        self.time_text = self.canvas.create_text(102, 130, text="00:00", fill="white", font=(C.FONT_NAME, 24, "bold"))
        self.canvas.grid(column=1, row=1)
        self.start_button = C.Button(text="Start", font=(C.FONT_NAME, 12, "bold"), borderwidth=5,
                                   command=self.start_timer)
        self.start_button.grid(column=0, row=4)
        self.reset_button = C.Button(text="Exit", font=(C.FONT_NAME, 12, "bold"), borderwidth=5,
                                   command=self.exit)
        self.reset_button.grid(column=2, row=4)
        self.Tick_mark = C.Label(text="", fg="green", bg="#A1B57D", font=(C.FONT_NAME, 18, "bold"))
        self.Tick_mark.grid(column=1, row=3)
        self.window.mainloop()

    def exit(self) -> None:
        C.sys.exit(0)

    def start_timer(self) -> None:
        """ start_timer() --> This function is responsible for password time to count_down function,
                            according to the promodoro timer.
        """
        global reps
        reps += 1

        work_time = C.WORK_MIN * 60
        short_break = C.SHORT_BREAK_MIN * 60
        long_break = C.LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            self.count_down(long_break)
            self.title.config(text="Break", fg="red")
        elif reps % 2 == 0:
            self.count_down(short_break)
            self.title.config(text="Break", fg="red")
        else:
            self.title.config(text="Work", fg="green")
            self.count_down(work_time)

    def count_down(self, count: int) -> None:
        """ count_down() --> This function is responsible for showing text and decreasing,
                            the time on the screen. It also shows how many time you have worked.
                            By show green tick mark on each time loop.

        Args:
            count (int): stores the time in seconds
        """
        minutes = C.math.floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f'0{seconds}'
        self.canvas.itemconfig(self.time_text, text=f'{minutes}:{seconds}')
        if count > 0:
            global my_timer
            my_timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            marks = ""
            for _ in range(C.math.floor(reps / 2)):
                marks += "✔"
            self.Tick_mark.config(text=marks)


if __name__ == "__main__":
    print("Running........")
    pt = pomodoro_timer()
