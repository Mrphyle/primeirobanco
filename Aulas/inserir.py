import mysql.connector as sqc
import pandas as pd
Marca =	input("Digite o nome da marca: ")
tipo_do_produto	= input("Digite o tipo do produto: ")
Codigo_de_barras = int(input("Digite o codigo de barras do produto: "))
descrição =	input("faça a descrição do produto: ")
valor = float(input("Digite o valor: "))
try:
    conexção = sqc.connect(
        host = 'localhost',
        user = 'root',
        password = "",
        database = 'mrphyledatabase',
    )
    cursor = conexção.cursor()
    comand_sql= f"INSERT INTO produto(Marca,tipo_do_produto,Codigo_de_barras,descrição,valor) VALUES({Marca},{tipo_do_produto},{Codigo_de_barras},{descrição},{valor})"
    cursor.execute(comand_sql)
    conexção.commit()
    print()
except:
    print("Não foi possivel se conectar")
finally:
    cursor.close()
    conexção.close()