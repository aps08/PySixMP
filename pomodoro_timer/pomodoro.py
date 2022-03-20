import math
from tkinter import *
import constants as C

reps = 0
my_timer = None


class pomodoro_timer:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Timer")
        self.window.resizable(False, False)
        self.window.config(padx=150, pady=75, bg=C.YELLOW)
        self.title = Label(text="Timer", fg=C.GREEN, bg=C.YELLOW, font=(C.FONT_NAME, 36, "bold"))
        self.title.grid(column=1, row=0)
        self.canvas = Canvas(width=200, height=224, bg=C.YELLOW, highlightthickness=0)
        self.IMG = PhotoImage(file=C.PATH)
        self.canvas.create_image(100, 112, image=self.IMG)
        self.time_text = self.canvas.create_text(102, 130, text="00:00", fill="white", font=(C.FONT_NAME, 24, "bold"))
        self.canvas.grid(column=1, row=1)
        self.start_button = Button(text="Start", font=(C.FONT_NAME, 10, "bold"), borderwidth=5,
                                   command=self.start_timer)
        self.start_button.grid(column=0, row=4)
        self.reset_button = Button(text="Reset", font=(C.FONT_NAME, 10, "bold"), borderwidth=5,
                                   command=self.reset_time)
        self.reset_button.grid(column=2, row=4)
        self.Tick_mark = Label(text="", fg=C.GREEN, bg=C.YELLOW, font=(C.FONT_NAME, 18, "bold"))
        self.Tick_mark.grid(column=1, row=3)
        self.window.mainloop()

    def reset_time(self) -> None:
        self.canvas.itemconfig(self.time_text, text="00:00")
        self.title.config(text="Work")
        global reps
        reps = 0

    def start_timer(self) -> None:
        global reps
        reps += 1

        work_time = C.WORK_MIN * 60
        short_break = C.SHORT_BREAK_MIN * 60
        long_break = C.LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            self.count_down(long_break)
            self.title.config(text="Break", fg=C.RED)
        elif reps % 2 == 0:
            self.count_down(short_break)
            self.title.config(text="Break", fg=C.RED)
        else:
            self.title.config(text="Work", fg=C.GREEN)
            self.count_down(work_time)

    def count_down(self, count: int) -> None:
        minutes = math.floor(count / 60)
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
            for _ in range(math.floor(reps / 2)):
                marks += "✔"
            self.Tick_mark.config(text=marks)


if __name__ == "__main__":
    print("Running........")
    pt = pomodoro_timer()
