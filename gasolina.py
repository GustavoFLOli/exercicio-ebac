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
grafico.set_title('Preço da Gasolina por Dia', fontsize=15)
grafico.set_xlabel('Dia', fontsize=12)
grafico.set_ylabel('Preço (R$)', fontsize=12)

#Marcação do preço mais alto, indicado por seta
max_venda = data['venda'].max()
max_dia = data[data['venda'] == max_venda]['dia'].values[0]
grafico.annotate(f'Máximo: R${max_venda}', xy=(max_dia, max_venda), xytext=(max_dia, max_venda + 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05))

#Salvando o gráfico no arquivo gasolina.png
fig = grafico.get_figure()
fig.savefig('gasolina.png')