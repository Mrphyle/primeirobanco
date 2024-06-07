import mysql.connector as sqc
class colunsandsqlcodes:
    def Colunas():
        Marca =	input("Digite o nome da marca: ")
        tipo_do_produto	= input("Digite o tipo do produto: ")
        Codigo_de_barras = int(input("Digite o codigo de barras do produto: "))
        descrição =	input("faça a descrição do produto: ")
        valor = float(input("Digite o valor: "))
        return Marca,tipo_do_produto,Codigo_de_barras 
    def sqlcodes():
        insert_marca= "INSERT INTO produto"
        return insert_marca
try:
    conexção = sqc.connect(
        host = 'localhost',
        user = 'root',
        password = "",
        database = 'mrphyledatabase',
    )
    print("conectado com susseso!")
except:
    print("Não foi possivel se conectar")