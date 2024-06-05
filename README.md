## grafico-preço-gasolina
Exercício de Git da EBAC - Gráfico de preço da gasolina


## Gráfico de Preço da Gasolina
Este projeto gera um gráfico de linha mostrando a variação do preço da gasolina ao longo de um período de dias, utilizando dados fornecidos em um arquivo CSV.

O gráfico é gerado usando as bibliotecas pandas e seaborn e é salvo em um arquivo PNG.

## Estrutura do Projeto
gasolina.csv: Arquivo CSV contendo os dados de preço da gasolina por dia.

gasolina.py: Script Python que lê os dados do CSV, gera o gráfico de linha e salva o gráfico como um arquivo PNG.

## Estrutura do Arquivo CSV
O arquivo gasolina.csv deve ter a seguinte estrutura:

```csv 
dia,venda 
1,5.11 
2,4.99 
3,5.02 
4,5.21 
5,5.07 
6,5.09 
7,5.13 
8,5.12 
9,4.94 
10,5.03
```

## Dependências

### Pandas

[Pandas](https://pandas.pydata.org/) é uma biblioteca poderosa e fácil de usar para análise e manipulação de dados em Python. Ela é particularmente útil para trabalhar com dados tabulares, como arquivos CSV. Pandas oferece estruturas de dados e ferramentas de análise de dados de alto desempenho e fáceis de usar.

### Seaborn

[Seaborn](https://seaborn.pydata.org/) é uma biblioteca Python para visualização de dados baseada no Matplotlib. Ela fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos. Seaborn é ideal para criar gráficos complexos com poucas linhas de código.

Você pode instalar essas dependências usando pip:

```
pip install pandas seaborn 
```

## Executando o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.

2. Instale as dependências necessárias usando pip:


```
pip install pandas seaborn
```

3. Certifique-se de que o arquivo gasolina.csv está no mesmo diretório que o script gasolina.py.

4. Execute o script gasolina.py:

```
python gasolina.py
```

5. O gráfico gerado será salvo no arquivo gasolina.png no mesmo diretório.