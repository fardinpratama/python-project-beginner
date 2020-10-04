from win10toast import ToastNotifier
import winsound
from tkinter import (Tk, Label, Entry, Frame, Button,
                     PhotoImage, Checkbutton, IntVar)
import tkinter.font as tkFont
import time
import website_blocker as wb


# set Notifier
toaster = ToastNotifier()
path_icon = "pomodoro technique notifier\logo.ico"


def focus(timer):
    # Show notification whenever needed
    label = "Start Focusing " + str(timer) + " minutes"
    toaster.show_toast("Pomodoro Notification!", label, threaded=True,
                       icon_path=path_icon, duration=5)  # 3 seconds
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    if var_1.get() == 1:
        wb.web_blocker(timer)
    else:
        time.sleep(timer)


def short_break_time(i, timer):
    until = 3
    label = "Take a short break " + \
        str(timer) + " minutes\n" + str(until-i) + " Pomodoro until long break"
    toaster.show_toast("Pomodoro Notification!", label, threaded=True,
                       icon_path=path_icon, duration=5)  # 3 seconds
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    time.sleep(timer)


def long_break_time(timer):
    label = "Take a long break " + str(timer) + " minutes"
    toaster.show_toast("Pomodoro Notification!", label, threaded=True,
                       icon_path=path_icon, duration=5)  # 3 seconds
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    time.sleep(timer)


def completed():
    toaster.show_toast("Pomodoro Notification!", "Taks is complete", threaded=True,
                       icon_path=path_icon, duration=5)  # 3 seconds
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


def start_pomodoro():
    app.withdraw()
    i = 0
    time_focus = int(input_focus.get())
    time_short_break = int(input_short_break.get())
    time_long_break = int(input_long_break.get())
    numb_set = int(input_set.get())
    while numb_set:
        focus(time_focus)
        if i < 3:
            short_break_time(i, time_short_break)
            i += 1
        else:
            if numb_set == 1:
                completed()
            else:
                long_break_time(time_long_break)
            numb_set -= 1
    else:
        app.deiconify()


# design GUI APP
app = Tk()
app.title("Pomodoro")
logo = PhotoImage(file='pomodoro technique notifier/logo.png')
app.iconphoto(False, logo)
app.geometry("200x245")
app.configure(bg="white")
bg_header = Frame(app, width=200, height=50, bg='#fb020c')
bg_header.grid(row=0, column=0, columnspan=2)
fontstyle = tkFont.Font(family="Helvetica", size=13)
header = Label(
    app, text="POMODORO TIMER \n With Python", anchor='center', font=fontstyle, bg='#fb020c', fg='white')
header.grid(row=0, column=0, columnspan=2)

label_duration = Label(
    app, text='Duration setting (minute)', bg='white', fg="#fb020c")
label_duration.grid(row=1, column=0, pady=5, sticky='s', columnspan=2)
# focus
focus_label = Label(
    app, text='Focus', bg='white', fg="#fb020c")
focus_label.grid(row=2, column=0, pady=5, padx=5, sticky='w')
input_focus = Entry(app, width=8, fg="#fb020c")
input_focus.grid(row=2, column=1, sticky='w')
input_focus.insert(0, "25")

# short Break
short_break_label = Label(
    app, text='Short break', bg='white', fg="#fb020c",)
short_break_label.grid(row=3, column=0, pady=5, padx=5, sticky='w')
input_short_break = Entry(app, width=8, fg="#fb020c")
input_short_break.grid(row=3, column=1, sticky='w')
input_short_break.insert(0, "5")

# long break
long_break_label = Label(
    app, text='Long break\n(after 4th focus)', justify='left', bg='white', fg="#fb020c")
long_break_label.grid(row=4, column=0, pady=0, padx=5, sticky='w')
input_long_break = Entry(app, width=8, fg="#fb020c")
input_long_break.grid(row=4, column=1, sticky='w')
input_long_break.insert(0, "15")

# check button website blocker
var_1 = IntVar()
web_block = Checkbutton(app, text="Block Socmed",
                        variable=var_1, bg='white', fg="#fb020c")
web_block.grid(row=5, column=0)

# set
set_label = Label(
    app, text='Set', justify='left', bg='white', fg="#727272")
set_label.grid(row=6, column=0)
input_set = Entry(app, width=4, fg="#727272")
input_set.grid(row=6, column=0, sticky='e', padx=10)
input_set.insert(0, "1")

# start
start = Button(
    app, text="start", command=start_pomodoro, bg='#fb020c', fg='white', width=5, font=fontstyle)
start.grid(row=6, column=1, pady=5, padx=5, columnspan=2, sticky='w')


app.mainloop()
