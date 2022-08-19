from mongoengine import Document, StringField, ListField, DecimalField


class Todo(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)

class Book(Document):
    book_name = StringField(required=True, max_length=200)
    category = ListField(StringField(max_length=100))
    rent_per_day = DecimalField(min_value=0)
