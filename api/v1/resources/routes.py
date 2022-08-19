from v1.resources.todos import todos
from v1.resources.books import books


def initialize_routes(api):
    api.add_namespace(todos)
    api.add_namespace(books)
