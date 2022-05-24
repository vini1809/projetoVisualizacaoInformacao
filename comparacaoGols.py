### importando bibliotecas
import pandas as pd
import warnings as wa
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

### ignorando warnings do tipo FutureWarning
wa.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None

### carrega datasets
path_periodo = "https://github.com/juvenalfonseca/python/blob/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-periodo.csv?raw=true"
path_jogos = "https://github.com/juvenalfonseca/python/blob/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-jogos.csv?raw=true"

df_periodo = pd.read_csv(path_periodo, delimiter=";")
df_jogos = pd.read_csv(path_jogos, delimiter=";")

### padroniza caixa dos nomes das variáveis
df_periodo.columns = df_periodo.columns.str.lower()
df_jogos.columns = df_jogos.columns.str.lower()

### altera campos de datas de character para date
df_periodo['inicio'] = pd.to_datetime(df_periodo['inicio'], format="%d/%m/%Y")
df_periodo['fim'] = pd.to_datetime(df_periodo['fim'], format="%d/%m/%Y")
df_jogos['data'] = pd.to_datetime(df_jogos['data'], format="%d/%m/%Y")

### captalizar strings
df_jogos['dia'] = df_jogos['dia'].str.title()
df_jogos['mandante'] = df_jogos['mandante'].str.title()
df_jogos['visitante'] = df_jogos['visitante'].str.title()
df_jogos['vencedor'] = df_jogos['vencedor'].str.title()
df_jogos['arena'] = df_jogos['arena'].apply(lambda x: x.title())

### junta os datasets e retorna apenas os registros corretos criados na junção
df_periodo['key'] = 1
df_jogos['key'] = 1

df = pd.merge(df_periodo, df_jogos, on='key').drop("key", 1)
df = df.query('data >= inicio & data <= fim')

gols_corinthians_mandante = df.loc[df['mandante'] == 'Corinthians']['mandante placar'].sum()
gols_corinthians_visitante = df.loc[df['visitante'] == 'Corinthians']['visitante placar'].sum()
gols_corinthians_total = gols_corinthians_mandante + gols_corinthians_visitante
gols_corinthians_media = gols_corinthians_total / 17

gols_flamengo_mandante = df.loc[df['mandante'] == 'Flamengo']['mandante placar'].sum()
gols_flamengo_visitante = df.loc[df['visitante'] == 'Flamengo']['visitante placar'].sum()
gols_flamengo_total = gols_flamengo_mandante + gols_flamengo_visitante
gols_flamengo_media = gols_flamengo_total / 17

gols_palmeiras_mandante = df.loc[df['mandante'] == 'Palmeiras']['mandante placar'].sum()
gols_palmeiras_visitante = df.loc[df['visitante'] == 'Palmeiras']['visitante placar'].sum()
gols_palmeiras_total = gols_palmeiras_mandante + gols_palmeiras_visitante
gols_palmeiras_media = gols_palmeiras_total / 17

gols_atletico_mandante = df.loc[df['mandante'] == 'Atlético-Mg']['mandante placar'].sum()
gols_atletico_visitante = df.loc[df['visitante'] == 'Atlético-Mg']['visitante placar'].sum()
gols_atletico_total = gols_atletico_mandante + gols_atletico_visitante
gols_atletico_media = gols_atletico_total / 17

gols_saopaulo_mandante = df.loc[df['mandante'] == 'São Paulo']['mandante placar'].sum()
gols_saopaulo_visitante = df.loc[df['visitante'] == 'São Paulo']['visitante placar'].sum()
gols_saopaulo_total = gols_saopaulo_mandante + gols_saopaulo_visitante
gols_saopaulo_media = gols_saopaulo_total / 17

categories = ['Gols Mandante', 'Gols Visitante', 'Gols Total', 'Media Gols']
categories = [*categories, categories[0]]

corinthians = [gols_corinthians_mandante, gols_corinthians_visitante, gols_corinthians_total, gols_corinthians_media]
flamengo = [gols_flamengo_mandante, gols_flamengo_visitante, gols_flamengo_total, gols_flamengo_media]
palmeiras = [gols_palmeiras_mandante, gols_palmeiras_visitante, gols_palmeiras_total, gols_palmeiras_media]
atletico = [gols_atletico_mandante, gols_atletico_visitante, gols_atletico_total, gols_atletico_media]
saopaulo = [gols_saopaulo_mandante, gols_saopaulo_visitante, gols_saopaulo_total, gols_saopaulo_media]
corinthians = [*corinthians, corinthians[0]]
flamengo = [*flamengo, flamengo[0]]
palmeiras = [*palmeiras, palmeiras[0]]
atletico = [*atletico, atletico[0]]
saopaulo = [*saopaulo, saopaulo[0]]

label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(corinthians))

plt.figure(figsize=(12, 8), edgecolor='#000000', facecolor='#E5E5E5')
plt.subplot(2, 2, 1, polar=True)
plt.fill(label_loc, corinthians, '#000000')
plt.plot(label_loc, corinthians, '#000000', label='Corinthians')
plt.title('Corinthians', size=12)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories, size=8)
plt.suptitle('Comparação de gols no Campeonato Brasileiro entre os anos 2003 - 2020', fontsize=16)
plt.subplot(2, 2, 2, polar=True)
plt.fill(label_loc, flamengo, '#ff0000')
plt.plot(label_loc, flamengo, '#ff0000', label='Flamengo')
plt.title('Flamengo', size=12)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories, size=8)
plt.subplot(2, 2, 3, polar=True)
plt.fill(label_loc, palmeiras, '#008d00')
plt.plot(label_loc, palmeiras, '#008d00', label='Palmeiras')
plt.title('Palmeiras', size=12)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories, size=8)
plt.subplot(2, 2, 4, polar=True)
plt.fill(label_loc, atletico, '#ffffff')
plt.plot(label_loc, atletico, '#000000', label='Atlético-Mg')
plt.title('Atlético-Mg', size=12)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories, size=8)
plt.subplots_adjust(left=0.122,
                    bottom=0.105,
                    right=0.9,
                    top=0.88,
                    wspace=0.189,
                    hspace=0.38)
plt.show()
