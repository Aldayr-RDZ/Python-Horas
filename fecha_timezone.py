from calendar import calendar, monthrange
from datetime import *


import pytz
import dateutil.relativedelta
import pandas as pd
import requests
import json

today = datetime.datetime.now()
timezone= pytz.timezone('America/Monterrey')
aware = datetime.datetime.now(timezone)
print("dia",aware.strftime("%Y-%m-%d"))
print("hora",aware.strftime("%H:%M:%S"))
print("-------------------------")
print(today.strftime("El dia  %Y-%m-%d"))
print(today.strftime("%H:%M:%S"))

print(calendar.monthrange(2022,4))



for tz in pytz.all_timezones:
    print (tz)

from time import gmtime, strftime
import time
print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))

from datetime import datetime
from datetime import timezone

now = datetime.now(timezone.utc)
Date = now.strftime("%a, %d %b %Y %H:%M:%S GMT")

today=time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
print(today)
print(now)
print(Date)


def fecha_hoy(Fecha_separada = False):
    timezone=pytz.timezone('America/Monterrey')
    today = datetime.now(timezone)
    if Fecha_separada == False:
        fecha = today
        return fecha
    else:
        mes = today.month
        dia = today.day
        anio = today.year
        return mes, dia, anio