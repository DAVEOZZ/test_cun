from infraestructure.repositories import ItemRepository


class AddClientCommand:
    def __init__(self, name: str):
        self.name = name

class AddClientHandler:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def handle(self, command: AddClientCommand):
        return self.repository.add_client(command.name)