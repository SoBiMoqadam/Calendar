# 📅 Python Calendar

<div align="center">
<h1 style="color:#00FFFF; font-family:monospace;">🗓 Python Calendar</h1>
<p style="font-family:monospace; font-size:18px; color:#9be7ff;">
A smart calendar to check dates, switch calendar types, and toggle themes effortlessly 🚀
</p>
</div>

---

## ✨ Features

- ✅ **Today's Date**: Quickly find the date of the day & month  
- 🔄 **Switch Calendar Type**: Toggle between Solar (Persian) & Gregorian  
- 🌗 **Themes**: Light and Dark background options  
- 🎨 **Clean Interface** with smooth interactions  

---

## 💻 Sample Code

<div style="background: #1e1e2f; padding: 15px; border-radius: 12px; font-family: monospace; color: #fff; line-height:1.6; box-shadow: 0 5px 15px rgba(0,0,0,0.3); margin: 20px 0;">
<pre style="color:#f8f8f2;">
import tkinter as tk
from persiantools.jdatetime import JalaliDate
from datetime import date, datetime
import calendar

# Sample: Display today's date
current_date = JalaliDate.today()
print("Today's date:", current_date)

# Switch between calendar types
calendar_type = "jalali"  # or "gregorian"

# Toggle themes
theme = "light"  # or "dark"
</pre>
</div>

---

## 🛠 Installation / Setup

<div style="background: linear-gradient(135deg, #222, #444); border-radius:12px; padding:20px; font-family:monospace; font-size:14px; color:#fff; line-height:1.6; box-shadow: 0 5px 15px rgba(0,0,0,0.3); margin:20px 0;">
Clone the repository and run:

<pre style="background:#111; padding:10px; border-radius:8px;">
git clone https://github.com/SoBiMoqadam/Python-Calendar.git
cd Python-Calendar
python main.py
</pre>
</div>

---

## 🔥 Download Full File

<div style="display:flex; justify-content:center; margin:20px 0;">
  <a href="https://github.com/SoBiMoqadam/Python-Calendar/raw/main/main.py" 
     target="_blank"
     style="
        padding:12px 30px;
        font-size:16px;
        font-weight:bold;
        color:white;
        text-decoration:none;
        border-radius:8px;
        background: linear-gradient(135deg, #FF1493, #FF69B4);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s, box-shadow 0.2s;
     "
     onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 10px 20px rgba(0,0,0,0.4)';"
     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 5px 15px rgba(0,0,0,0.3)';"
  >
      ⬇️ Download main.py
  </a>
</div>

---

Made with ❤️ using Python
