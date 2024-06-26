from infraestructure.repositories import ItemRepository


class AddProductCommand:
    def __init__(self, name: str):
        self.name = name

class AddProductHandler:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def handle(self, command: AddProductCommand):
        return self.repository.add_product(command.name)