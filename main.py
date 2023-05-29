import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo Excel
df = pd.read_excel('caminho/para/o/arquivo.xlsx')

# Visualização dos primeiros registros do DataFrame
print(df.head())

# Verificando informações gerais do DataFrame
print(df.info())

# Análise estatística descritiva dos dados numéricos
print(df.describe())

# Visualização de dados: Gráfico de barras
df['Coluna'].value_counts().plot(kind='bar')
plt.title('Contagem por categoria')
plt.xlabel('Categoria')
plt.ylabel('Contagem')
plt.show()

# Trabalhando com datas: Convertendo coluna para tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Criando colunas de ano e mês
df['Ano'] = df['Data'].dt.year
df['Mês'] = df['Data'].dt.month

# Total de ocorrências por ano
ocorrencias_por_ano = df['Ano'].value_counts().sort_index()

# Total de ocorrências por mês
ocorrencias_por_mes = df.groupby('Mês')['Coluna'].count()

# Trabalhando com planilhas do Excel: Salvando um novo arquivo
df_novo = df[df['Coluna'] > 10]  # Filtrando dados

df_novo.to_excel('caminho/para/o/novo_arquivo.xlsx', index=False)

