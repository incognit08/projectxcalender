import calendar
from datetime import datetime

# Get the current year and month
now = datetime.now()
year = now.year
month = now.month

# Create a text calendar
cal = calendar.TextCalendar(calendar.SUNDAY)
cal_str = cal.formatmonth(year, month)

print("Here is the calendar for this month:\n")
print(cal_str)
