from flask import Flask, Blueprint, request, render_template
import pandas as pd

views = Blueprint('views', __name__)

gsheetid = "1spJY13t1JG08XqczqSm_78g4W3Krcje9mHLXQJAMI74"
gsheet_url = 'https://docs.google.com/spreadsheets/d/{}/edit#gid=566910442'.format(gsheetid)
url_1 = gsheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
df = pd.read_csv(url_1)

# arquivo = os.path.abspath('./app/dados/data_covid.csv')
# df = pd.read_csv(arquivo)

@views.route('/')
def hello():
    url_base = request.host_url
    url = url_base + "insight"  
    data = 'Selecione'

    return render_template('index.html', url=url, data=data, url_base=url_base)

@views.route('/insight1')
def qntd_casos():
    backgroundColor = "rgb(239, 35, 60, 0.5)"
    borderColor = "rgb(239, 35, 60)"
    url_base = request.host_url
    url = url_base + "insight"
    data = "Casos confirmados"
    typeChart = "line"    
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
    
    values = count_casos
    qntd = qntd
    labels = meses
    
    return render_template('index.html', borderColor=borderColor, backgroundColor=backgroundColor, url_base=url_base, url=url, typeChart=typeChart, data = data, values = values, qntd = qntd, labels = labels)

@views.route('/insight2')
def insight2():
    backgroundColor = "rgb(65, 105, 225, 0.5)"
    borderColor = "rgb(65, 105, 225)"
    url_base = request.host_url
    url = url_base + "insight"
    data = "Quantidade de pessoas vacinadas"
    typeChart = "bar"
    anos = []
    count_vacinados = [] 
    
    df['ano'] = df['date'].str[0:4]
    
    for x in range(len(df)):
        ano = df['ano'][x]
        anos.append(ano)
        vacinados = 0
        for y in range(len(df)):
            if ano == df['ano'][y]:
                vacinados = df['total_vaccinations'][y]
                vacinados = vacinados + vacinados
        count_vacinados.append(vacinados)
    
    anos = list(dict.fromkeys(df['date'].str[0:4]))
    count_vacinados = list(dict.fromkeys(count_vacinados))
    values = count_vacinados
    labels = anos
    
    return render_template('index.html', borderColor=borderColor, backgroundColor=backgroundColor, url_base=url_base, url=url, typeChart=typeChart, data = data, values = values, labels = labels)

@views.route('/insight3')
def insight3():
    url_base = request.host_url
    url = url_base + "insight"
    typeChart = "line"
    data = "Quantidade de pessoas vacinadas"
    backgroundColor = "rgb(50, 205, 50, 0.5)"
    borderColor = "rgb(50, 205, 50)"
    data1 = "Quantidade de mortes"
    backgroundColor1 = "rgb(29, 29, 29, 0.5)"
    borderColor1 = "rgb(29, 29, 29)"

    anos = []
    count_vacinados = []
    count_mortes = []
    
    df['ano_mes'] = df['date'].str[0:4]
    
    for x in range(len(df)):
        ano = df['ano_mes'][x]
        anos.append(ano)
        vacinados = 0
        mortes = 0
        for y in range(len(df)):
            if ano == df['ano_mes'][y]:
                vacinados = df['total_vaccinations'][y]
                vacinados = vacinados + vacinados
                
                mortes = df['new_deaths'][y]
                mortes = mortes + mortes
        count_vacinados.append(vacinados)
        count_mortes.append(mortes)
    
    
    anos = list(dict.fromkeys(anos))
    count_vacinados = list(dict.fromkeys(count_vacinados))
    print(count_vacinados)
    count_mortes = list(dict.fromkeys(count_mortes))
    values = count_vacinados
    values1 = count_mortes
    labels = anos
    
    return render_template('twolines.html', data1=data1, backgroundColor1=backgroundColor1, borderColor1=borderColor1, values1=values1, borderColor=borderColor, backgroundColor=backgroundColor, url_base=url_base, url=url, typeChart=typeChart, data = data, values = values, labels = labels)

@views.route('/insight4')
def insight4():
    url_base = request.host_url
    url = url_base + "insight"  
    data = 'dev'

    return render_template('index.html', url=url, data=data, url_base=url_base)

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