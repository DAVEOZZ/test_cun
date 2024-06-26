from domain.models import get_db_connection

class ItemRepository:
    def __init__(self):
        self.conn = get_db_connection()

    def add_item(self, id_client: int,id_product:int):
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO orders (id_client,id_product) VALUES (%s,%s) RETURNING *", (id_client,id_product))
            item = cursor.fetchone()
            self.conn.commit()
            return item
        
    def add_client(self, name: str):
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO clients (name_client) VALUES (%s) RETURNING *", (name,))
            client = cursor.fetchone()
            self.conn.commit()
            return client

    def add_product(self, name: str):
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO products (name_product) VALUES (%s) RETURNING *", (name,))
            product = cursor.fetchone()
            self.conn.commit()
            return product     

    def get_items(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT clients.name_client, products.name_product FROM orders inner join clients on orders.id_client=clients.id_client inner join products on orders.id_product=products.id_product")
            items = cursor.fetchall()
            return items
        

    def get_clients(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clients")
            clients = cursor.fetchall()
            return clients
        
    def get_products(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return products
