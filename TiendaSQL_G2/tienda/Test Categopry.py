from tienda.Category import Category
from tienda.Conexion import Conexion

conexion = Conexion(host='localhost', port=3306, user='root', password="", database='tienda_sura_2')

conexion.connnect_db()




category = Category(None, None)

#category.create_category(conexion)

category.delete_category(conexion, 1)





