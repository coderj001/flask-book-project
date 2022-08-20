from v1.resources.books import books
from v1.resources.transactions import transactions


def initialize_routes(api):
    api.add_namespace(books)
    api.add_namespace(transactions)
