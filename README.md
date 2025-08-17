# 📅 Python Calendar

<div align="center">
<h1 style="color:#00ffff; font-family:monospace;">🗓 Python Calendar</h1>
<p style="font-family:monospace; font-size:16px; color:#9be7ff;">
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

```python
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
