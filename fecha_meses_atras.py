from funciones import Meses_atras
from calendar import calendar, monthrange
from datetime import *


import pytz
import dateutil.relativedelta
import pandas as pd
import requests
import json

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

# MESES_ATRAS = 6
def Ejemplo2():
    Fecha_end= fecha_hoy(False)
    mes, dia, anio = fecha_hoy(True)
    last_day =monthrange(anio, mes)[1]
    start = date(anio, mes, 1)
    end_month = date(anio,mes,last_day)
    MESES_ATRAS = Meses_atras(dia=dia)
    if MESES_ATRAS == 0:
        Fecha_start = start
    else:
        start= f"{anio}-{mes}-{1}"
        fechastr = datetime.strptime(start, "%Y-%m-%d")
        Fecha_start = fechastr - dateutil.relativedelta.relativedelta(months=MESES_ATRAS)
        
    
    print(Fecha_start)
    

    
    while Fecha_start.strftime("%Y-%m-%d") <= Fecha_end.strftime("%Y-%m-%d"):
            # print(Fecha_start.strftime("%m-%d"))
            # print(Fecha_end.strftime("%m-%d"))
            # print("Fecha_start : ",Fecha_start) 
            Fecha_end_aux_str = Fecha_end.strftime("%Y-%m-%d")
            Fecha_start_str= Fecha_start.strftime("%Y-%m-%d")
            Fecha_end_month_str = end_month.strftime("%Y-%m-%d")
            fecha1 = datetime.strptime(Fecha_start_str,  "%Y-%m-%d")
            fecha2 = datetime.strptime(Fecha_end_aux_str,  "%Y-%m-%d")
            fecha3 = datetime.strptime(Fecha_end_month_str,  "%Y-%m-%d")
            
            res = fecha2 - fecha1
            # res2 = fecha3 - fecha2
            # res3 = fecha3 - fecha1
            # semanas = res / timedelta(weeks=1)
            # semanas2 = res2 /timedelta(weeks=1)
            dias_entre_fecha2_fecha1 = res / timedelta(days=1)
            if dias_entre_fecha2_fecha1 <7:
                Fecha_end_aux = Fecha_start + timedelta(days= dias_entre_fecha2_fecha1)
            else:
                Fecha_end_aux = Fecha_start + timedelta(days=7)
            # Fecha_end_aux = Fecha_start + timedelta(days=7)
            print("lo que va en el dic",Fecha_start.strftime("%Y-%m-%d"))
            print("lo que va en el dic",Fecha_end_aux.strftime("%Y-%m-%d"))
            Fecha_start = Fecha_end_aux + timedelta(days=1)

            print(int(dias_entre_fecha2_fecha1))
            # if int(dias_entre_fecha2_fecha1) <=7:
            #     Fecha_end_aux = Fecha_start + timedelta(days=int(dias_entre_fecha2_fecha1))
            #     print("Fecha_start más 8 dias : ",Fecha_end_aux)
            #     Fecha_start = Fecha_end_aux + timedelta(days=int(dias_entre_fecha2_fecha1))
            #     print("Fecha_start_new1: ",Fecha_start)
            #     print("FIINAAAL")
            # else:
            #     Fecha_end_aux = Fecha_start + timedelta(days=7)
            #     print("Fecha_start más 8 dias : ",Fecha_end_aux)
                
            #     print("Fecha_start_new2: ",Fecha_start)
            #     print("FIINAAAL")
            
            # print("lo que va en el dic",Fecha_start)
            # print("lo que va en el dic",Fecha_end_aux)
            # Fecha_start = Fecha_end_aux + timedelta(days=1)
            # print("Fecha_start_new: ",Fecha_start)

            # print("Fecha_start más 8 dias : ",Fecha_end_aux)
Ejemplo2()