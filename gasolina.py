#Importando os pacotes utilizados 
import pandas as pd
import seaborn as sns

#Carregando os dados do arquivo gasolina.csv
data = pd.read_csv('gasolina.csv')

#Configurando o estilo do gráfico
sns.set(style='whitegrid')

#Criando o gráfico de linha com os dados do arquivo csv
grafico = sns.lineplot(x='dia', y='venda', data=data, marker='o')

#Definindo o título e os rótulos do gráfico
grafico.set_title('Preço da Gasolina por Dia')
grafico.set_xlabel('Dia')
grafico.set_ylabel('Preço (R$)')

#Salvando o gráfico no arquivo gasolina.png
fig = grafico.get_figure()
fig.savefig('gasolina.png')