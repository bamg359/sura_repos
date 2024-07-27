from tienda.Conexion import Conexion

from fastapi import FastAPI, Body

from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello":"world"}

db = Conexion(host='localhost', port=3306, user='root', password="", database='tienda_sura_2')
db.connnect_db()

class Category:
    category_id = None
    category_name = None

    def __init__(self, category_id, category_name):
        self._category_id = category_id
        self._category_name = category_name

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        self._category_id = category_id

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        self._category_name = category_name




    @staticmethod
    def from_row(row):
        return Category(row[0], row[1])


    @app.post('/create_category/{category_id, category_name}', tags=["Registrar categoria"])
    def create_category(category_id: int = Body(), category_name: str = Body()):
        #self._category_id = int(input("id"))
        #self._category_name = input("Nombre categoria")
        query = "INSERT INTO category(category_name)VALUES(%s)"
        params = (category_name,)
        db.execute_query(query, params)


    @staticmethod
    @app.get('/get_categpry/', tags= ["Listar Categorias"])
    def select_category():
        query = "SELECT * FROM category"
        result = db.execute_query(query)
        if result:
            categories = []
            for row in result:
                category = Category.from_row(row)
                categories.append(category)
                print(row[0], row[1])
            return categories
        else:
            print("Categorias no encontradas")
            return []

    @app.delete('/delete_category/', tags=["Delete_category"])
    def delete_category(category_id:int = Body()):
        query = "DELETE FROM category WHERE category_id = %s"
        db.execute_query(query, (category_id,))



    @app.put('/update_category/{category_id, category_name}', tags=["Actualizar Categoria"])
    def update_category(category_id:int= Body(), category_name:str = Body()):
        #self._category_name = input("Ingrese el nuevo nombre de la categoria")
        query = "UPDATE category SET category_name = %s WHERE category_id = %s"
        values = (category_name, category_id)
        db.execute_query(query, values)






