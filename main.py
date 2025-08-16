import tkinter as tk
from persiantools.jdatetime import JalaliDate
from datetime import date, datetime
import calendar

events_shamsi = {
    (11, 22): "پیروزی انقلاب اسلامی",
    (3, 14): "رحلت امام خمینی"
}

calendar_type = "jalali"
theme = "light"
current_date = JalaliDate.today()
current_year = current_date.year
current_month = current_date.month

def apply_theme():
    global bg_color, fg_color, header_bg, button_bg, event_fg, current_day_bg, button_fg

    if theme == "light":
        bg_color = "#e0f0ff"
        fg_color = "#004080"
        header_bg = "#cce6ff"
        button_bg = "#a3c1da"
        event_fg = "#b22222"
        current_day_bg = "#add8e6"
        button_fg = "#003366"
    else:
        bg_color = "#0f0f0f"
        fg_color = "#00e0ff"
        header_bg = "#1a1a1a"
        button_bg = "#003344"
        event_fg = "#aa4444"
        current_day_bg = "#003344"
        button_fg = "#00e0ff"

    root.configure(bg=bg_color)
    for frame in [cal_frame, event_frame, today_frame, button_frame]:
        frame.configure(bg=bg_color)

    label_main_date.configure(bg=bg_color, fg=fg_color, font=("Yekan Bakh", 16, "bold"))
    label_alt_date.configure(bg=bg_color, fg=fg_color, font=("Yekan Bakh", 12))

    for btn in [btn_prev, btn_type, btn_next, btn_theme]:
        btn.configure(bg=button_bg, fg=button_fg, bd=2, relief="raised", padx=15, pady=8, cursor="hand2")

    update_calendar()
    show_today()

def update_calendar():
    for widget in cal_frame.winfo_children():
        widget.destroy()

    weekdays_jalali = ["شنبه", "یک‌شنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه"]
    weekdays_gregorian = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    if calendar_type == "jalali":
        this_month = JalaliDate(current_year, current_month, 1)
        g_date = JalaliDate(current_year, current_month, 15).to_gregorian()  # استفاده از روز وسط ماه
        month_range = calendar.monthrange(g_date.year, g_date.month)[1]
        first_day_weekday = this_month.weekday()
        weekdays = weekdays_jalali
        col_index_func = lambda i: 6 - i  # نمایش از راست به چپ
        label_main_date.config(text=f"{this_month.strftime('%B %Y')}")
        label_alt_date.config(text=f"{g_date.strftime('%B %Y')}")
    else:
        this_month = datetime(current_year, current_month, 1)
        month_range = calendar.monthrange(current_year, current_month)[1]
        first_day_weekday = (calendar.monthrange(current_year, current_month)[0] + 1) % 7
        weekdays = weekdays_gregorian
        col_index_func = lambda i: i
        label_main_date.config(text=f"{this_month.strftime('%B %Y')}")
        j_date = JalaliDate(datetime(current_year, current_month, 15))
        label_alt_date.config(text=f"{j_date.strftime('%B %Y')}")

    for i, day in enumerate(weekdays):
        col_index = col_index_func(i)
        lbl = tk.Label(cal_frame, text=day, font=("Yekan Bakh", 11, "bold"),
                       bg=header_bg, fg=fg_color, bd=1, relief="solid")
        lbl.grid(row=0, column=col_index, sticky="nsew", padx=1, pady=1)

    days = ["" for _ in range(first_day_weekday)] + list(range(1, month_range + 1))
    rows = [days[i:i + 7] for i in range(0, len(days), 7)]

    today_jalali = JalaliDate.today()
    today_gregorian = date.today()

    for r, week in enumerate(rows):
        for c in range(7):
            day = week[c] if c < len(week) else ""
            bg = bg_color
            fg = fg_color
            note = ""

            if isinstance(day, int):
                if calendar_type == "jalali":
                    if (today_jalali.year, today_jalali.month, today_jalali.day) == (current_year, current_month, day):
                        bg = current_day_bg
                    if (current_month, day) in events_shamsi:
                        bg = "#ffe4e1" if theme == "light" else "#552222"
                        note = events_shamsi[(current_month, day)]
                        fg = event_fg
                else:
                    if (today_gregorian.year, today_gregorian.month, today_gregorian.day) == (current_year, current_month, day):
                        bg = current_day_bg
                    j_date = JalaliDate(datetime(current_year, current_month, day))
                    if (j_date.month, j_date.day) in events_shamsi:
                        note = events_shamsi[(j_date.month, j_date.day)]
                        fg = event_fg
                        bg = "#ffe4e1" if theme == "light" else "#552222"

            col_index = col_index_func(c)

            lbl = tk.Label(cal_frame, text=f"{day}\n{note}", font=("Yekan Bakh", 11),
                           fg=fg, bg=bg, bd=1, relief="ridge",
                           anchor="center", justify="center")
            lbl.grid(row=r + 1, column=col_index, sticky="nsew", padx=1, pady=1)

    for i in range(7):
        cal_frame.columnconfigure(i, weight=1)
    for i in range(len(rows) + 1):
        cal_frame.rowconfigure(i, weight=1)

    for widget in event_frame.winfo_children():
        widget.destroy()
    tk.Label(event_frame, text="📅 مناسبت‌های این ماه:", font=("Yekan Bakh", 12, "bold"),
             fg=fg_color, bg=bg_color, anchor="e", justify="right").pack(anchor="e", pady=(0, 4))
    for (m, d), title in events_shamsi.items():
        if m == current_month:
            tk.Label(event_frame, text=f"روز {d} – {title}", font=("Yekan Bakh", 11),
                     bg=bg_color, fg=event_fg, anchor="e", justify="right").pack(anchor="e")

def prev_month():
    global current_month, current_year
    current_month -= 1
    if current_month < 1:
        current_month = 12
        current_year -= 1
    update_calendar()

def next_month():
    global current_month, current_year
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
    update_calendar()

def toggle_calendar_type():
    global calendar_type, current_year, current_month
    if calendar_type == "jalali":
        today = date.today()
        current_year, current_month = today.year, today.month
        calendar_type = "gregorian"
    else:
        today = JalaliDate.today()
        current_year, current_month = today.year, today.month
        calendar_type = "jalali"
    update_calendar()

def toggle_theme():
    global theme
    theme = "dark" if theme == "light" else "light"
    apply_theme()

def show_today():
    for widget in today_frame.winfo_children():
        widget.destroy()
    today_j = JalaliDate.today()
    today_g = date.today()
    tk.Label(today_frame, text=f"📌 Today (Gregorian): {today_g.strftime('%d %B %Y')}",
             font=("Yekan Bakh", 11), bg=bg_color, fg=fg_color).pack()
    tk.Label(today_frame, text=f"📌 امروز (شمسی): {today_j.strftime('%d %B %Y')}",
             font=("Yekan Bakh", 11), bg=bg_color, fg=fg_color).pack()

root = tk.Tk()
root.title("تقویم شمسی/میلادی")
root.geometry("750x750")
root.resizable(True, True)

label_main_date = tk.Label(root, text="")
label_main_date.pack(pady=(10, 0))
label_alt_date = tk.Label(root, text="")
label_alt_date.pack()

today_frame = tk.Frame(root)
today_frame.pack(pady=10)

cal_frame = tk.Frame(root)
cal_frame.pack(fill="both", expand=True, pady=10)


event_frame = tk.Frame(root)
event_frame.pack(pady=(0, 10))

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_prev = tk.Button(button_frame, text="ماه قبل", command=prev_month, font=("Yekan Bakh", 11, "bold"), width=12)
btn_type = tk.Button(button_frame, text="نوع تقویم", command=toggle_calendar_type, font=("Yekan Bakh", 11, "bold"), width=12)
btn_next = tk.Button(button_frame, text="ماه بعد", command=next_month, font=("Yekan Bakh", 11, "bold"), width=12)
btn_theme = tk.Button(button_frame, text="تم دارک و لایت", command=toggle_theme, font=("Yekan Bakh", 11, "bold"), width=26)

btn_prev.grid(row=0, column=0, padx=5)
btn_type.grid(row=0, column=1, padx=5)
btn_next.grid(row=0, column=2, padx=5)
btn_theme.grid(row=1, column=0, columnspan=3, pady=8)

apply_theme()
root.mainloop()
