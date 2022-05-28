import pandas as pd
import warnings as wa
import matplotlib.pyplot as plt
import numpy as np

wa.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None

path_periodo = "https://github.com/juvenalfonseca/python/blob/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-periodo.csv?raw=true"
path_jogos = "https://github.com/juvenalfonseca/python/blob/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-jogos.csv?raw=true"

df_periodo = pd.read_csv(path_periodo, delimiter=";")
df_jogos = pd.read_csv(path_jogos, delimiter=";")

df_periodo.columns = df_periodo.columns.str.lower()
df_jogos.columns = df_jogos.columns.str.lower()

df_periodo['inicio'] = pd.to_datetime(df_periodo['inicio'], format="%d/%m/%Y")
df_periodo['fim'] = pd.to_datetime(df_periodo['fim'], format="%d/%m/%Y")
df_jogos['data'] = pd.to_datetime(df_jogos['data'], format="%d/%m/%Y")

df_jogos['dia'] = df_jogos['dia'].str.title()
df_jogos['mandante'] = df_jogos['mandante'].str.title()
df_jogos['visitante'] = df_jogos['visitante'].str.title()
df_jogos['vencedor'] = df_jogos['vencedor'].str.title()
df_jogos['arena'] = df_jogos['arena'].apply(lambda x: x.title())

df_periodo['key'] = 1
df_jogos['key'] = 1

df = pd.merge(df_periodo, df_jogos, on='key').drop("key", 1)
df = df.query('data >= inicio & data <= fim')

SPmandante = df.loc[df['estado mandante'] == 'SP']['estado vencedor'].count()
MGmandante = df.loc[df['estado mandante'] == 'MG']['estado vencedor'].count()
RJmandante = df.loc[df['estado mandante'] == 'RJ']['estado vencedor'].count()
SPvisitante = df.loc[df['estado visitante'] == 'SP']['estado vencedor'].count()
MGvisitante = df.loc[df['estado visitante'] == 'MG']['estado vencedor'].count()
RJvisitante = df.loc[df['estado visitante'] == 'RJ']['estado vencedor'].count()
sptotal = SPmandante + SPvisitante
mgtotal = MGmandante + MGvisitante
rjtotal = RJmandante + RJvisitante

estados = ['SÃO PAULO', 'MINAS GERAIS', 'RIO DE JANEIRO']

data = [sptotal, mgtotal, rjtotal]

explode = (0.1, 0.0, 0.0)
colors = ("cyan", "grey", "indigo",)
wp = {'linewidth': 1, 'edgecolor': "black"}


def func(pct, allvalues):
    absolute = int(pct / 100. * np.sum(allvalues))
    return "{:.1f}%\n({:d} v)".format(pct, absolute)


fig, ax = plt.subplots(figsize=(10, 7), edgecolor='#000000', facecolor='#FEE312')
wedges, texts, autotexts = ax.pie(data,
                                  autopct=lambda pct: func(pct, data),
                                  explode=explode,
                                  labels=estados,
                                  shadow=True,
                                  colors=colors,
                                  startangle=90,
                                  wedgeprops=wp,
                                  textprops=dict(color="black"))
ax.legend(wedges, estados,
          title="Estados",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Vitorias por estado Campeonato Brasileiro 2003-2020", size=24)
plt.show()