from flask import Flask, send_file
import pandas as pd
import numpy as np  # linear algebra
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar o arquivo CSV
df = pd.read_csv('./static/kaggle/apple_quality.csv')

df.dropna(inplace=True)  # remover linhas ou colunas de um DataFrame do pandas que contenham valores ausentes

df = df.drop(['A_id'], axis=1)

# Gera o gráfico de coluna sobre a qualidade
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Quality')
plt.title('Quality')
plt.savefig('static/images/quality_plot.png')  # Salvar o gráfico como uma imagem PNG
plt.close()  # Fechar a figura para liberar memória

# size vs weight
plt.figure(figsize=(4, 4), dpi=150)
sns.scatterplot(data=df, x='Weight', y='Size', alpha=0.5)
plt.savefig('static/images/size_weight_plot.png')  # Salvar o gráfico como uma imagem PNG
plt.close()  # Fechar a figura para liberar memória

# Size vs sweetness
plt.figure(figsize=(4, 4), dpi=150)
sns.scatterplot(data=df, x='Sweetness', y='Size', alpha=0.5)
plt.savefig('static/images/size_sweetness_plot.png')  # Salvar o gráfico como uma imagem PNG
plt.close()  # Fechar a figura para liberar memória

# size vs Crunchiness
plt.figure(figsize=(4, 4), dpi=150)
sns.scatterplot(data=df, x='Crunchiness', y='Size', alpha=0.5)
plt.savefig('static/images/size_Crunchiness_plot.png')  # Salvar o gráfico como uma imagem PNG
plt.close()  # Fechar a figura para liberar memória

# Size vs Juiciness
plt.figure(figsize=(4, 4), dpi=150)
sns.scatterplot(data=df, x='Juiciness', y='Size', alpha=0.5)
plt.savefig('static/images/size_Juiciness_plot.png')  # Salvar o gráfico como uma imagem PNG
plt.close()  # Fechar a figura para liberar memória

# Size vs Ripeness
plt.figure(figsize=(4, 4), dpi=150)
sns.scatterplot(data=df, x='Ripeness', y='Size', alpha=0.5)
plt.savefig('static/images/size_Ripeness_plot.png')  # Salvar o gráfico como uma imagem PNG
plt.close()  # Fechar a figura para liberar memória

# Size vs Acidity
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Acidity', y='Size')
plt.savefig('static/images/size_Acidity_plot.png')  # Salvar o gráfico como uma imagem PNG
plt.close()  # Fechar a figura para liberar memória

# criar variáveis dummy (variáveis binárias) a partir de uma variável categórica no DataFrame
# Cria 2 colunas: Bad e Good, e atribui o valor 0 ou 1).
quality_dummies = pd.get_dummies(df['Quality'], dtype='int')

# Concatena as variáveis binárias ao database.
df = pd.concat([df, quality_dummies], axis=1)

# Exclui a coluna Quality
df = df.drop(['Quality'], axis=1)

# Cria o gráfico de heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='Blues')
# Salva o gráfico como uma imagem PNG na pasta static/images
plt.savefig('static/images/heatmap.png')
# Fecha a figura para liberar memória
plt.close()

app = Flask(__name__)


@app.route('/')
def index():
    return send_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
