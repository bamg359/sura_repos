

class product:

    product_id = None
    product_name = None
    category = None
    description = None
    price = None
    quantity = None
    brand = "My own brand"

    def __init__(self, product_id, product_name, category, description, price, quantity, brand):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.description = description
        self.price = price
        self.quantity = quantity
        self.brand = brand


    #Getters and Setters


    def create_product(self):
        self.product_id = input("id Producto")
