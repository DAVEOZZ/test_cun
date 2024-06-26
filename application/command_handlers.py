from infraestructure.repositories import ItemRepository

class AddItemCommand:
    def __init__(self, id_client:int, id_product:int):
        self.id_client = id_client
        self.id_product = id_product

class AddItemHandler:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def handle(self, command: AddItemCommand):
        return self.repository.add_item(command.id_client,command.id_product)
    


