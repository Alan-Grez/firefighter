import pandas as pd
import plotly.express as px


def graf_sinis(tipo_fecha, df):
    """
        Grafica en función de la fecha medidas en tipo_fecha
    
    """
    months = {1:'Enero', 2:'Febrero', 3:'Marzo'      ,  4:'Abril'  ,  5:'Mayo'     ,  6:'Junio', 7:'Julio', 8:'Agosto' , 9:'Septiembre' , 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

    weeks  = dict([tuple((i,"semana {numero_semana}".format(numero_semana = i))) for i in range(1,52)] )

    days   = dict([tuple((i,"Día {numero_semana}".format(numero_semana = i))) for i in range(1,32)] )
    
    df_aux = df.copy()
    if tipo_fecha == "dias" or tipo_fecha == "dia":
        df_aux.fecha = df.fecha.apply(lambda x: x.day)
        df_aux       = df_aux.assign(fecha = lambda x: x['fecha'].replace(days) )
        x_min, x_max = -0.5,12
        y_min, y_max = 0, 50
        titulo = "Gráfico N°Siniestros/Día"
        
    if tipo_fecha == "semana" or tipo_fecha == "semanas":
        df_aux.fecha = df.fecha.apply(lambda x: x.week)
        df_aux       = df_aux.assign(fecha = lambda x: x['fecha'].replace(weeks) )
        x_min, x_max = -0.5,12
        y_min, y_max = 0, 50
        titulo = "Gráfico N°Siniestros/Semana"
        
    if tipo_fecha == "mes" or tipo_fecha == "meses":
        df_aux.fecha = df.fecha.apply(lambda x: x.month)
        df_aux       = df_aux.assign(fecha = lambda x: x['fecha'].replace(months) )
        x_min, x_max = -0.5,12
        y_min, y_max = 0, 135
        titulo = "Gráfico N°Siniestros/Mes"
    
    return px.histogram(df_aux, 
        x="tipo_de_servicio",
        color="tipo_de_servicio", 
        # add the animation
        animation_frame="fecha",
        category_orders = {"tipo_de_servicio":['10.0','10.1','10.2','10.3','10.4','10.5','10.6','10.7','10.9','10.12','10.13','6.16']},
        labels = {"tipo_de_servicio":"Clave"},
        range_x = [x_min, x_max],
        range_y = [y_min, y_max],
        title = titulo,
        
    )
     