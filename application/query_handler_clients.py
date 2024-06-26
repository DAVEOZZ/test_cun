from infraestructure.repositories import ItemRepository

class GetClientsQuery:
    pass

class GetClientsHandler:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def handle(self, query: GetClientsQuery):
        return self.repository.get_clients()
