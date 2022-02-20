import datetime
from re import T
import pytz


today = datetime.datetime.now()
timezone= pytz.timezone('US/Hawaii')
aware = datetime.datetime.now(timezone)
print("dia",aware.strftime("%Y-%m-%d"))
print("hora",aware.strftime("%H:%M:%S"))
print("-------------------------")
print(today.strftime("El dia  %Y-%m-%d"))
print(today.strftime("%H:%M:%S"))




# for tz in pytz.all_timezones:
#     print (tz)