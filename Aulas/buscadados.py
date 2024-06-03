import mysql.connector as sqc
import pandas as pd
from sqlalchemy import create_engine
config = {
    'user':'hoolf',
    'password':'0718',
    'host': 'localhost',
    'database': 'mrphyledatabase'
}
conect = sqc.connect(**config)
query = "SELECT * FROM "
df = pd.read_sql_query(query, conect)
print("Dados lidos do banco de dados:")
print(df.head())

# Fechando a conexão
conect.close()