import pandas as pd
import warnings as wa
import seaborn as sns
import matplotlib.pyplot as plt

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

gols_mandante = df[['torneio', 'mandante placar']].groupby('torneio').agg(lambda x: sum(x)).reset_index()
gols_mandante.rename(columns={"mandante placar": "gols_mandante"}, inplace=True)

gols_visitante = df.groupby('torneio')['visitante placar'].sum().sort_values(ascending=False).reset_index()
gols_visitante.rename(columns={"visitante placar": "gols_visitante"}, inplace=True)

gols_edicao = pd.merge(gols_mandante, gols_visitante, on="torneio")
gols_edicao['gols_total'] = gols_edicao['gols_mandante'] + gols_edicao['gols_visitante']
gols_edicao['gols_mandante_perc'] = (gols_edicao['gols_mandante'] / gols_edicao['gols_total']) * 100
gols_edicao['gols_visitantes_perc'] = (gols_edicao['gols_visitante'] / gols_edicao['gols_total']) * 100

gols_edicao

df1 = gols_edicao[['torneio', 'gols_mandante']]
df2 = gols_edicao[['torneio', 'gols_visitante']]
df3 = gols_edicao[['torneio', 'gols_total']]

df1.rename(columns={'gols_mandante': 'gols'}, inplace=True)
df2.rename(columns={'gols_visitante': 'gols'}, inplace=True)
df3.rename(columns={'gols_total': 'gols'}, inplace=True)

df1['tipo_gols'] = 'gols_mandante'
df2['tipo_gols'] = 'gols_visitante'
df3['tipo_gols'] = 'gols_total'

df4 = pd.concat([df1, df2, df3]).reset_index(drop=True)

sns.set_style("darkgrid")
fig, ax = plt.subplots(figsize=(15.5, 8), facecolor='#FEE312')
custom_palette = ["black", "purple", "orange"]
sns.set_palette(custom_palette)
sns.barplot(x="torneio", y="gols", hue="tipo_gols", data=df4)
plt.title('Gols do Brasileirão')
plt.show()