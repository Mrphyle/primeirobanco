#imports
import pandas
import plotly.express as px
#importar base de dados
#visualização da base de dados
file = r"C:\Users\hoolf\Desktop\sinchouse\sincpyhouse\Python power up\cancelamentos_sample.csv"
tabela = pandas.read_csv(file)
#tratamento da base de dados
tabela.drop(columns="CustomerID")
tabela.dropna()
#analize de canselamento
tabela["cancelou"].value_counts(normalize=True)
#causa do canselamento
graph= px.histogram(tabela, x="canselou")
graph.show()
