### importando bibliotecas
import pandas as pd
import warnings as wa
import seaborn as sns
import matplotlib.pyplot as plt

### ignorando warnings do tipo FutureWarning
wa.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None

### carrega datasets
path_periodo = "https://github.com/juvenalfonseca/python/blob/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-periodo.csv?raw=true"
path_jogos = "https://github.com/juvenalfonseca/python/blob/master/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-jogos.csv?raw=true"

df_periodo = pd.read_csv(path_periodo, delimiter=";")
df_jogos = pd.read_csv(path_jogos, delimiter=";")

