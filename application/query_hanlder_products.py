from infraestructure.repositories import ItemRepository

class GetProductsQuery:
    pass

class GetProductsHandler:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def handle(self, query: GetProductsQuery):
        return self.repository.get_products()