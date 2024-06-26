from infraestructure.repositories import ItemRepository

class GetItemsQuery:
    pass

class GetItemsHandler:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def handle(self, query: GetItemsQuery):
        return self.repository.get_items()
    


