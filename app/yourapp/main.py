from flask import Flask, Blueprint, request, render_template
import pandas as pd
import os

views = Blueprint('views', __name__)

arquivo = os.path.abspath('./app/dados/data_covid.csv')
df = pd.read_csv(arquivo)

@views.route('/')
def hello():
    count_casos = []
    meses = []
    df['ano_mes'] = df['date'].str[0:7]
    
    for x in range(len(df)):
        ano_mes = df['ano_mes'][x]
        meses.append(ano_mes)
        casos = 0
        for y in range(len(df)):
            if ano_mes == df['ano_mes'][y]:
                casos = df['new_cases'][y]
                casos = casos + casos
        count_casos.append(casos)
    
    meses = list(dict.fromkeys(meses))
    count_casos = list(dict.fromkeys(count_casos))
    qntd = len(count_casos)

    return render_template('index.html', values = count_casos, qntd = qntd, labels = meses)

@views.route('/gjs')
def graf():
    params = {
        "x":["A","B","C","D","E","F","G"],
        "y":[100,120,100,50,80,90,120],
        "nomes":["Eq","Valores"]
    }
    params2 = {
        "x":["Blue","Red","Cian","Black","Pink","White","Green"],
        "y":[60,100,40,80,90,70,10],
        "nomes":["Times","Notas"]
    }

    x = params['x']
    y = params['y']
    x2=params2['x']
    y2=params2['y']

    # return render_template( 'graficoXY_JS.html', labels=x, values=y )   # mostra a tela com grafico
    return render_template( 'index.html', labels=x, values=y, labels2=x2, values2=y2 )   # mostra a tela com grafico