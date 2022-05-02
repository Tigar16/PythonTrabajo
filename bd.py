import pymysql
"""Funcion para la conexion con la base de mysql"""

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='bdsbfacturacion')