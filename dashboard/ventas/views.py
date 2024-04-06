from django.shortcuts import render
from django.http import HttpResponse
from dash import Dash, html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd

def dashboard(request):
    # Datos
    datos = [
    {"barrio": "Barrio1", "mes": "Enero", "ventas": 15000},
    {"barrio": "Barrio2", "mes": "Enero", "ventas": 12000},
    {"barrio": "Barrio3", "mes": "Enero", "ventas": 13500},
    {"barrio": "Barrio4", "mes": "Enero", "ventas": 11000},
    {"barrio": "Barrio5", "mes": "Enero", "ventas": 10000},
    
    {"barrio": "Barrio1", "mes": "Febrero", "ventas": 16000},
    {"barrio": "Barrio2", "mes": "Febrero", "ventas": 12500},
    {"barrio": "Barrio3", "mes": "Febrero", "ventas": 14000},
    {"barrio": "Barrio4", "mes": "Febrero", "ventas": 11500},
    {"barrio": "Barrio5", "mes": "Febrero", "ventas": 10500},
    
    {"barrio": "Barrio1", "mes": "Marzo", "ventas": 16500},
    {"barrio": "Barrio2", "mes": "Marzo", "ventas": 13000},
    {"barrio": "Barrio3", "mes": "Marzo", "ventas": 14500},
    {"barrio": "Barrio4", "mes": "Marzo", "ventas": 12000},
    {"barrio": "Barrio5", "mes": "Marzo", "ventas": 11000},
    
    {"barrio": "Barrio1", "mes": "Abril", "ventas": 17000},
    {"barrio": "Barrio2", "mes": "Abril", "ventas": 13500},
    {"barrio": "Barrio3", "mes": "Abril", "ventas": 15000},
    {"barrio": "Barrio4", "mes": "Abril", "ventas": 12500},
    {"barrio": "Barrio5", "mes": "Abril", "ventas": 11500},
    
    {"barrio": "Barrio1", "mes": "Mayo", "ventas": 17500},
    {"barrio": "Barrio2", "mes": "Mayo", "ventas": 14000},
    {"barrio": "Barrio3", "mes": "Mayo", "ventas": 15500},
    {"barrio": "Barrio4", "mes": "Mayo", "ventas": 13000},
    {"barrio": "Barrio5", "mes": "Mayo", "ventas": 12000},
    
    {"barrio": "Barrio1", "mes": "Junio", "ventas": 18000},
    {"barrio": "Barrio2", "mes": "Junio", "ventas": 14500},
    {"barrio": "Barrio3", "mes": "Junio", "ventas": 16000},
    {"barrio": "Barrio4", "mes": "Junio", "ventas": 13500},
    {"barrio": "Barrio5", "mes": "Junio", "ventas": 12500},
    
    {"barrio": "Barrio1", "mes": "Julio", "ventas": 18500},
    {"barrio": "Barrio2", "mes": "Julio", "ventas": 15000},
    {"barrio": "Barrio3", "mes": "Julio", "ventas": 16500},
    {"barrio": "Barrio4", "mes": "Julio", "ventas": 14000},
    {"barrio": "Barrio5", "mes": "Julio", "ventas": 13000},
    
    {"barrio": "Barrio1", "mes": "Agosto", "ventas": 19000},
    {"barrio": "Barrio2", "mes": "Agosto", "ventas": 15500},
    {"barrio": "Barrio3", "mes": "Agosto", "ventas": 17000},
    {"barrio": "Barrio4", "mes": "Agosto", "ventas": 14500},
    {"barrio": "Barrio5", "mes": "Agosto", "ventas": 13500},
    
    {"barrio": "Barrio1", "mes": "Septiembre", "ventas": 19500},
    {"barrio": "Barrio2", "mes": "Septiembre", "ventas": 16000},
    {"barrio": "Barrio3", "mes": "Septiembre", "ventas": 17500},
    {"barrio": "Barrio4", "mes": "Septiembre", "ventas": 15000},
    {"barrio": "Barrio5", "mes": "Septiembre", "ventas": 14000},
    
    {"barrio": "Barrio1", "mes": "Octubre", "ventas": 20000},
    {"barrio": "Barrio2", "mes": "Octubre", "ventas": 16500},
    {"barrio": "Barrio3", "mes": "Octubre", "ventas": 18000},
    {"barrio": "Barrio4", "mes": "Octubre", "ventas": 15500},
    {"barrio": "Barrio5", "mes": "Octubre", "ventas": 14500},
    
    {"barrio": "Barrio1", "mes": "Noviembre", "ventas": 20500},
    {"barrio": "Barrio2", "mes": "Noviembre", "ventas": 17000},
    {"barrio": "Barrio3", "mes": "Noviembre", "ventas": 18500},
    {"barrio": "Barrio4", "mes": "Noviembre", "ventas": 16000},
    {"barrio": "Barrio5", "mes": "Noviembre", "ventas": 15000},
    
    {"barrio": "Barrio1", "mes": "Diciembre", "ventas": 21000},
    {"barrio": "Barrio2", "mes": "Diciembre", "ventas": 17500},
    {"barrio": "Barrio3", "mes": "Diciembre", "ventas": 19000},
    {"barrio": "Barrio4", "mes": "Diciembre", "ventas": 16500},
    {"barrio": "Barrio5", "mes": "Diciembre", "ventas": 15500},
    
    {"barrio": "Barrio6", "mes": "Enero", "ventas": 13000},
    {"barrio": "Barrio7", "mes": "Enero", "ventas": 12500},
    {"barrio": "Barrio8", "mes": "Enero", "ventas": 14000},
    {"barrio": "Barrio9", "mes": "Enero", "ventas": 11500},
    {"barrio": "Barrio10", "mes": "Enero", "ventas": 11000},
    
    {"barrio": "Barrio6", "mes": "Febrero", "ventas": 13500},
    {"barrio": "Barrio7", "mes": "Febrero", "ventas": 13000},
    {"barrio": "Barrio8", "mes": "Febrero", "ventas": 14500},
    {"barrio": "Barrio9", "mes": "Febrero", "ventas": 12000},
    {"barrio": "Barrio10", "mes": "Febrero", "ventas": 11500},
    
    {"barrio": "Barrio6", "mes": "Marzo", "ventas": 14000},
    {"barrio": "Barrio7", "mes": "Marzo", "ventas": 13500},
    {"barrio": "Barrio8", "mes": "Marzo", "ventas": 15000},
    {"barrio": "Barrio9", "mes": "Marzo", "ventas": 12500},
    {"barrio": "Barrio10", "mes": "Marzo", "ventas": 12000},
    
    {"barrio": "Barrio6", "mes": "Abril", "ventas": 14500},
    {"barrio": "Barrio7", "mes": "Abril", "ventas": 14000},
    {"barrio": "Barrio8", "mes": "Abril", "ventas": 15500},
    {"barrio": "Barrio9", "mes": "Abril", "ventas": 13000},
    {"barrio": "Barrio10", "mes": "Abril", "ventas": 12500},
    
    {"barrio": "Barrio6", "mes": "Mayo", "ventas": 15000},
    {"barrio": "Barrio7", "mes": "Mayo", "ventas": 14500},
    {"barrio": "Barrio8", "mes": "Mayo", "ventas": 16000},
    {"barrio": "Barrio9", "mes": "Mayo", "ventas": 13500},
    {"barrio": "Barrio10", "mes": "Mayo", "ventas": 13000},
    
    {"barrio": "Barrio6", "mes": "Junio", "ventas": 15500},
    {"barrio": "Barrio7", "mes": "Junio", "ventas": 15000},
    {"barrio": "Barrio8", "mes": "Junio", "ventas": 16500},
    {"barrio": "Barrio9", "mes": "Junio", "ventas": 14000},
    {"barrio": "Barrio10", "mes": "Junio", "ventas": 13500},
    
    {"barrio": "Barrio6", "mes": "Julio", "ventas": 16000},
    {"barrio": "Barrio7", "mes": "Julio", "ventas": 15500},
    {"barrio": "Barrio8", "mes": "Julio", "ventas": 17000},
    {"barrio": "Barrio9", "mes": "Julio", "ventas": 14500},
    {"barrio": "Barrio10", "mes": "Julio", "ventas": 14000},
    
    {"barrio": "Barrio6", "mes": "Agosto", "ventas": 16500},
    {"barrio": "Barrio7", "mes": "Agosto", "ventas": 16000},
    {"barrio": "Barrio8", "mes": "Agosto", "ventas": 17500},
    {"barrio": "Barrio9", "mes": "Agosto", "ventas": 15000},
    {"barrio": "Barrio10", "mes": "Agosto", "ventas": 14500},
    
    {"barrio": "Barrio6", "mes": "Septiembre", "ventas": 17000},
    {"barrio": "Barrio7", "mes": "Septiembre", "ventas": 16500},
    {"barrio": "Barrio8", "mes": "Septiembre", "ventas": 18000},
    {"barrio": "Barrio9", "mes": "Septiembre", "ventas": 15500},
    {"barrio": "Barrio10", "mes": "Septiembre", "ventas": 15000},
    
    {"barrio": "Barrio6", "mes": "Octubre", "ventas": 17500},
    {"barrio": "Barrio7", "mes": "Octubre", "ventas": 17000},
    {"barrio": "Barrio8", "mes": "Octubre", "ventas": 18500},
    {"barrio": "Barrio9", "mes": "Octubre", "ventas": 16000},
    {"barrio": "Barrio10", "mes": "Octubre", "ventas": 15500},
    
    {"barrio": "Barrio6", "mes": "Noviembre", "ventas": 18000},
    {"barrio": "Barrio7", "mes": "Noviembre", "ventas": 17500},
    {"barrio": "Barrio8", "mes": "Noviembre", "ventas": 19000},
    {"barrio": "Barrio9", "mes": "Noviembre", "ventas": 16500},
    {"barrio": "Barrio10", "mes": "Noviembre", "ventas": 16000},
    
    {"barrio": "Barrio6", "mes": "Diciembre", "ventas": 18500},
    {"barrio": "Barrio7", "mes": "Diciembre", "ventas": 18000},
    {"barrio": "Barrio8", "mes": "Diciembre", "ventas": 19500},
    {"barrio": "Barrio9", "mes": "Diciembre", "ventas": 17000},
    {"barrio": "Barrio10", "mes": "Diciembre", "ventas": 16500}
]


    # Convertir la lista de diccionarios a DataFrame
    df = pd.DataFrame(datos)

    # Inicializar la aplicación Dash
    app = Dash(__name__)

    # Layout de la aplicación Dash
    app.layout = html.Div([
        dcc.Graph(id='ventas-por-mes', figure={})
    ])

    # Callback para actualizar el gráfico
    @app.callback(
        Output('ventas-por-mes', 'figure'),
        Input('ventas-por-mes', 'value')
    )
    def update_figure(selected_value):
        if not selected_value:
            raise PreventUpdate
        fig = px.bar(df, x='mes', y='ventas', color='barrio', title='Ventas por Mes y Barrio')
        return fig

    # Convertir la aplicación Dash a HTML
    html_content = app.index()

    # Renderizar el HTML
    return HttpResponse(html_content)

