
# MESES_ATRAS = 1
# def listaDeFechas():
#     Fecha = fecha_hoy(False)
#     mes, dia, anio  = fecha_hoy(True)

#     # print(Fecha.strftime('%Y-%m-%d'))
#     # Fecha = Fecha - timedelta(days=1)
#     # print(Fecha.strftime('%Y-%m-%d'))
#     Tope = Fecha.strftime("%m")
#     while Tope == Fecha.strftime("%m"):
#         print("Fecha DATE: ", Fecha.strftime('%Y-%m-%d'))
#         fecha = Fecha.strftime('%Y-%m-%d')
#         print("Fecha String: ", fecha)
#         Fecha = Fecha - timedelta(days=1)


# def listaDeFechasMes():
    
#     Fecha= fecha_hoy(False)
#     mes, dia, anio = fecha_hoy(True)
#     last_day =monthrange(anio, mes)[1]
#     start = date(anio, mes, 1)
#     if MESES_ATRAS == 0:
#         Fecha_start = start
#     else:
#         start= f"{anio}-{mes}-{1}"
#         fechastr = datetime.strptime(start, "%Y-%m-%d")
#         Fecha_start = fechastr - dateutil.relativedelta.relativedelta(months=MESES_ATRAS)
#     Tope = Fecha_start.strftime("%m")
#     while Tope <= Fecha.strftime('%m'):
        
#         print("Fecha DATE: ", Fecha.strftime('%Y-%m-%d'))
#         fecha = Fecha.strftime('%Y-%m-%d')
#         print("Fecha String: ", fecha)
#         Fecha = Fecha - timedelta(days=1)



# # listaDeFechas()


# from datetime import *

# epoch_time = 1650384000
# time_val = datetime.fromtimestamp(epoch_time)
# print('Date:', time_val)

# fecha = 1 
# print(fecha)
# fecha ^= 2
# print(fecha)

# def listaDeFechasMes():
    
#     Fecha_end= fecha_hoy(False)
#     mes, dia, anio = fecha_hoy(True)
#     last_day =monthrange(anio, mes)[1]
#     start = date(anio, mes, 1)
#     if MESES_ATRAS == 0:
#         Fecha_start = start
#     else:
#         start= f"{anio}-{mes}-{1}"
#         fechastr = datetime.strptime(start, "%Y-%m-%d")
#         Fecha_start = fechastr - dateutil.relativedelta.relativedelta(months=MESES_ATRAS)
#         Fecha_end = date(Fecha_end)

    

    
#     while Fecha_start.strftime("%m-%d") <= Fecha_end.strftime('%m-%d'):
        
#             Fecha_end_aux = Fecha_start + timedelta(days=7)
            
#             print("INICIOOO")
#             print("Fecha_start : ",Fecha_start) 
#             Fecha_end_aux_str = Fecha_end.strftime("%Y-%m-%d")
#             Fecha_start_str= Fecha_start.strftime("%Y-%m-%d")
#             fecha1 = datetime.strptime(Fecha_start_str,  "%Y-%m-%d")
#             fecha2 = datetime.strptime(Fecha_end_aux_str,  "%Y-%m-%d")
            
#             res = fecha2 - fecha1
#             dias = res / timedelta(days=1)

#             print(Fecha_start)
#             print(Fecha_end_aux)

#             print("variable de dias",int(dias))
#             if int(dias) <= 7:
#                 Fecha_end_aux = Fecha_start + timedelta(days=int(dias))
#                 print("Fecha_start + 8 dias : ",Fecha_end_aux)
#                 Fecha_start = Fecha_end_aux + timedelta(days=int(dias))
#                 print("Fecha_start_aux: ",Fecha_start)
#                 print("FIINAAAL")
#             else:
#                 Fecha_end_aux = Fecha_start + timedelta(days=7)
#                 print("Fecha_start + 8 dias : ",Fecha_end_aux)
#                 Fecha_start = Fecha_end_aux + timedelta(days=1)
#                 print("Fecha_start_aux: ",Fecha_start)
#                 print("FIINAAAL")      

# def Meses_atras(dia):
#     if dia <=5:
#         MESES_ATRAS = 1
#         return MESES_ATRAS
#     else:
#         MESES_ATRAS= 0
#         return MESES_ATRAS


            
# def Ejemplo():
#     from datetime import datetime, timedelta

#     Fecha_end= fecha_hoy(False)
#     mes, dia, anio = fecha_hoy(True)
#     last_day =monthrange(anio, mes)[1]
#     start = date(anio, mes, 1)
#     if MESES_ATRAS == 0:
#         Fecha_start = start
#     else:
#         start= f"{anio}-{mes}-{1}"
#         fechastr = datetime.strptime(start, "%Y-%m-%d")
#         Fecha_start = fechastr - dateutil.relativedelta.relativedelta(months=MESES_ATRAS)
    
    
#     Fecha_end_str = Fecha_end.strftime("%Y-%m-%d")
#     Fecha_start_str= Fecha_start.strftime("%Y-%m-%d")
#     fecha1 = datetime.strptime(Fecha_start_str,  "%Y-%m-%d")
#     fecha2 = datetime.strptime(Fecha_end_str,  "%Y-%m-%d")
    


#     res = fecha1 - fecha2
#     dias = res / timedelta(days=1)
#     print(int(dias))

    

            
    # Fecha_ocho_dias = Fecha_start - timedelta(days=8)
    # print(Fecha.strftime("%Y-%m-%d"))
    # print(Fecha_start)
    # print(Fecha_ocho_dias)
    
    # while Tope <= Fecha.strftime('%m'):
        
    #         print("Fecha DATE: ", Fecha.strftime('%Y-%m-%d'))
    #         fecha = Fecha.strftime('%Y-%m-%d')
    #         print("Fecha String: ", fecha)
    #         Fecha = Fecha - timedelta(days=1)

# listaDeFechasMes()



