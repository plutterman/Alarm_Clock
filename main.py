# Payton Lutterman
# Alarm Clock
# Last Updated 9-10
import random
# Imports
import random as r
from tkinter import *
from tkinter import ttk
from tkinter import font
import calendar as cal
import time
import datetime as date_time
from assets.scripts.settings import *
from assets.scripts.alarms import *

# Global Variables
time_text = ""
root = ""
time_label = ""
is_mil = True
mil_std_toggle = ""
stop_bttn = ""
ui = None
top_ui = None
low = 0
high = 24
set_alarm_hr = ""
set_alarm_min = ""
tag_var = ""
am_tag = ""
pm_tag = ""
timezone_cb = ""
alarm_string = ""
alarm_on_off_toggle = ""
alarm_on = False
set_alarm_bttn = ""
alarm_playing = False
a_min = ""
snooze_bttn = False
cur_min = ""
cur_hour = ""
tag = ""
update_frames = ""

tz = MST

def get_time(tz):
    global cur_min
    global cur_hour
    global tag


    total_time = cal.timegm(time.gmtime())
    total_time += tz * 3600 # Convert timezone offset to seconds
    cur_sec = total_time % 60
    total_min = total_time // 60
    cur_min = total_min % 60
    total_hour = total_min // 60
    cur_hour = total_hour % 24
    #cur_hour += tz
    tag = ""

    if not is_mil:
        if cur_hour >= 12:
            tag = "PM"
        else:
            tag = "AM"
        if cur_hour > 12:
            cur_hour -= 12

    str_hour = str(cur_hour)
    str_min = str(cur_min)
    str_sec = str(cur_sec)
    if cur_sec < 10:
        str_sec = "0"+str(cur_sec)
    if cur_min < 10:
        str_min = "0" + str(cur_min)

    #if cur_sec%10 == 0:
        #root.configure(background=r.choice(colors))

    time_string = str.format("{0:>2}:{1}:{2} {3}",str_hour,str_min,str_sec,tag)
    if (time_string == alarm_string and cur_sec == 0) and (not alarm_playing):
        play_alarm()
    return time_string
    
def root_setup():
    root = Tk()
    root.title(TITLE)
    root.iconbitmap("Assets/imgs/clock.ico")
    root.geometry(geo_string)
    root.config(background = bg_color)
    root.config(cursor = cursor_style)
    return root

def create_widgets():
    global time_label
    global mil_std_toggle
    global stop_bttn
    global ui
    global top_ui
    global set_alarm_hr
    global set_alarm_min
    global tag_var
    global am_tag
    global pm_tag
    global timezone_cb
    global set_alarm_bttn

    time_label = Label(root,textvariable = time_text,foreground= "red",background=bg_color)
    time_label.place(x=WIDTH/2, y=HEIGHT/2, anchor=CENTER)

    #  UI
    top_ui = Frame(root, height = 50 , width=WIDTH, background=bg_color)
    top_ui = top_ui
    top_ui.place(x = 0, y = HEIGHT - 502)
    top_ui.pack_propagate(False)
    top_ui.pack(side = TOP, fill=X)

    ui = Frame(root, height = 50, width=WIDTH, background=bg_color)
    ui = ui
    ui.place(x = 0, y = HEIGHT - 50)
    ui.pack_propagate(False)
    ui.pack(side = BOTTOM, fill=X)

    uifont = font.Font(family="Times New Roman", size=15, weight="bold")
    uifont2 = font.Font(family="Impact", size=15,)

    # Alarm On Off Toggle
    alarm_on_off_toggle = Checkbutton(top_ui, text="Alarm On/Off", command=alarm_on_off, font=uifont, bg=bg_color, fg="red")
    alarm_on_off_toggle.pack(side=LEFT)

    # Military Time Toggle
    mil_std_toggle= Checkbutton(top_ui,text="STD", command= toggle_std, font=uifont, bg=bg_color,fg="red")
    mil_std_toggle.pack(side=LEFT)

    # Set AM/PM
    am_pm_box = Frame(top_ui)
    tag_var = StringVar(am_pm_box, value = 0)
    am_tag = Radiobutton(am_pm_box, text="AM", variable=tag_var, value="AM", bg=bg_color,fg="red", width=2)
    am_tag.config(state=DISABLED)
    pm_tag = Radiobutton(am_pm_box, text="PM", variable=tag_var, value="PM", bg=bg_color,fg="red", width=2)
    pm_tag.config(state=DISABLED)
    am_tag.pack(side=TOP)
    pm_tag.pack(side=BOTTOM)
    am_pm_box.pack(side=RIGHT)
    set_alarm_bttn = Button(top_ui, text="Set Alarm", command=set_alarm, height=3, width=8, font=uifont, bg=bg_color, fg="red")
    set_alarm_bttn.config(state=DISABLED)

    # Timezone Selector Combobox
    timezone_cb = ttk.Combobox(top_ui, values=["EST","CST","MST","PST"], width=5, justify="center", height=35, font=uifont)
    timezone_cb.pack(side= LEFT)
    timezone_cb.current(2)
    timezone_cb.bind("<<ComboboxSelected>>", set_timezone)
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TCombobox", fieldbackground=bg_color, foreground="red", width = 5, lightcolor= bg_color)

    # Set Alarm
    set_alarm_min = Spinbox(top_ui, from_=0, to=59, justify="center", width=2, font=uifont, bg=bg_color,fg="red")
    set_alarm_min.config(state=DISABLED)
    set_alarm_min.pack(side=RIGHT)
    set_alarm_hr = Spinbox(top_ui, from_=low, to=high, justify="center", width=2, font=uifont, bg=bg_color,fg="red")
    set_alarm_hr.config(state=DISABLED)
    set_alarm_hr.pack(side=RIGHT)
    set_alarm_bttn.pack(side=RIGHT)

    # Stop Button
    stop_bttn = Button(ui, text="STOP", command=stop_alarm, height=40, width=12, font=uifont2, bg= "red", fg= "white")
    stop_bttn.pack(side=LEFT, fill=X, expand=True)

    # Snooze Button
    snooze_bttn = Button(ui, text="SNOOZE", command=snooze, height=40, width=10, font=uifont, bg=bg_color,fg="red")
    snooze_bttn.pack(side=LEFT, fill=X, expand=True)

def set_timezone(trash):
    global tz
    temp = timezone_cb.get()
    if temp == "EST":
        tz = EST
    if temp == "CST":
        tz = CST
    if temp == "MST":
        tz = MST
    if temp == "PST":
        tz = PST
def set_alarm():
    global alarm_string

    print("Alarm Set")

    a_hour = set_alarm_hr.get()
    a_min = set_alarm_min.get()

    if int(a_min) < 10:
        a_min = "0" + a_min
    a_sec = "00"
    a_tag = ""

    if is_mil:
        a_tag = ""
    else:
        a_tag = tag_var.get()
    alarm_string = str.format("{0:>2}:{1}:{2} {3}", a_hour, a_min, a_sec, a_tag)

def alarm_on_off():
    global alarm_on
    global set_alarm_bttn
    global stop_bttn
    global snooze_bttn

    alarm_on= not alarm_on
    if alarm_on:
        # Disable tz std
        mil_std_toggle.config(state=DISABLED)
        timezone_cb.config(state=DISABLED)
        # Enable set alarm bttn
        set_alarm_hr.config(state=NORMAL)
        set_alarm_min.config(state=NORMAL)
        set_alarm_bttn.config(state=NORMAL)

    else:
        # Enable tz std
        mil_std_toggle.config(state=NORMAL)
        timezone_cb.config(state=NORMAL)
        # Disable set alarm bttn
        set_alarm_hr.config(state=DISABLED)
        set_alarm_min.config(state=DISABLED)
        set_alarm_bttn.config(state=DISABLED)

def snooze():
    global snooze_bttn
    global alarm_string
    a_sec = "00"
    a_min = cur_min + 5
    a_hour = cur_hour
    if a_min >= 60:
        a_min - 60
        a_hour += 1

    pg.mixer.music.set_volume(10)

    alarm_string = str.format("{0:>2}:{1}:{2} {3}", a_hour, a_min, a_sec, tag)
    stop_alarm()
def stop_alarm():
    global alarm_playing

    alarm_playing = False
    pg.mixer.music.stop()
def play_alarm():
    global alarm_playing

    alarm_playing = True
    num = r.randint(0,1)
    if num == 0:
        alarm2()
    elif num == 1:
        alarm3()

def toggle_std():
    global is_mil
    global high
    global low

    is_mil = not is_mil

    if is_mil:
        high = 24
        low = 0
        am_tag.config(state=DISABLED)
        pm_tag.config(state=DISABLED)
    else:
        high = 12
        low = 1
        am_tag.config(state=NORMAL)
        pm_tag.config(state=NORMAL)

    set_alarm_hr.config(from_=low, to=high)


def update_widgets():
    global ui
    global top_ui

    # Get Current Height and Width
    w = root.winfo_width()
    h = root.winfo_height()

    # Update Widgets
    size = int(root.winfo_height() * .2)
    time_font = font.Font(family="Times New Roman", size=size, weight="bold")
    time_label.config(font=time_font)
    time_label.place(x=w / 2, y=h / 2, anchor=CENTER)

def run_clock():

    # Get New Time
    time_text.set(get_time(tz))
    update_widgets()
    root.after(1,run_clock)

def main():
    global time_text
    global root

    pg.mixer.init()
    root = root_setup()
    time_text = StringVar()
    time_text.set(get_time(tz))
    create_widgets()
    root.after(1, run_clock)
    root.mainloop()
main()
