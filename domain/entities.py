from domain.models import get_db_connection
from pydantic import BaseModel
from typing import Optional


def __init__(self):
        db_table()

def db_table():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS clients (id_client SERIAL PRIMARY KEY, name_client VARCHAR(255) NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS products (id_product SERIAL PRIMARY KEY, name_product VARCHAR(255) NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS orders (id_order SERIAL PRIMARY KEY, id_client INTEGER NOT NULL, id_product INTEGER NOT NULL, FOREIGN KEY (id_client) REFERENCES clients(id_client), FOREIGN KEY (id_product) REFERENCES products(id_product))")
        conn.commit()
        cur.close()
        conn.close()


class clients(BaseModel):
    id_client: int
    name_client: str
   

class products(BaseModel):
    id_product: int
    name_product: str

class orders(BaseModel):
    id_order: int
    id_client: Optional[clients] = None
    id_product: Optional[products] = None
    

    





