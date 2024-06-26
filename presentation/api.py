import json
import threading
from fastapi import FastAPI
from application.command_handlers import AddItemCommand, AddItemHandler
from application.command_handler_client import AddClientCommand, AddClientHandler
from application.command_handler_product import AddProductCommand, AddProductHandler
from application.query_handlers import GetItemsQuery, GetItemsHandler
from application.query_handler_clients import GetClientsHandler,GetClientsQuery
from application.query_hanlder_products import GetProductsHandler,GetProductsQuery
from infraestructure.repositories import ItemRepository
from infraestructure.rabbitmq import RabbitMQ
from domain.entities import db_table


db_table= db_table()
app = FastAPI()
rabbitmq = RabbitMQ()


@app.post("/clients/")
def add_client(name: str):
    repository = ItemRepository()
    handler = AddClientHandler(repository)
    command = AddClientCommand(name)
    client = handler.handle(command)
    return client

@app.post("/products/")
def add_product(name: str):
    repository = ItemRepository()
    handler = AddProductHandler(repository)
    command = AddProductCommand(name)
    product = handler.handle(command)
    return product

@app.post("/orders/")
def add_item(id_client: int,id_product: int):
    repository = ItemRepository()
    handler = AddItemHandler(repository)
    command = AddItemCommand(id_client,id_product)
    item = handler.handle(command)
    return item


@app.get("/clients")
def get_clients():
    repository = ItemRepository()
    handler = GetClientsHandler(repository)
    query = GetClientsQuery()
    clients = handler.handle(query)
    return clients

@app.get("/products")
def get_products():
    repository = ItemRepository()
    handler = GetProductsHandler(repository)
    query = GetProductsQuery()
    products = handler.handle(query)
    return products


@app.get("/orders/")
def get_items():
    repository = ItemRepository()
    handler = GetItemsHandler(repository)
    query = GetItemsQuery()
    items = handler.handle(query)
    return items


@app.post("/orders/async/")
async def add_item_async(id_client: int, id_product: int):
    message = json.dumps({"id_client": id_client, "id_product": id_product})
    rabbitmq.send_message("pedido_queues_1", message)
    return {"message": "Solicitud de Creacion de Pedido"}

def on_message(ch, method, properties, body):
    data = json.loads(body)
    id_client = data.get("id_client")
    id_product = data.get("id_product")
    repository = ItemRepository()
    handler = AddItemHandler(repository)
    command = AddItemCommand(id_client, id_product)
    handler.handle(command)

# Start consuming messages
def start_consuming():
    rabbitmq.receive_message("pedido_queues_1", on_message)

thread = threading.Thread(target=start_consuming)
thread.start()
