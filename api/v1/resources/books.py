import json
from flask import abort
from flask_restx import Namespace, Resource
from v1.database.models import Book
from mongoengine import DoesNotExist


books = Namespace('v1/books', description='Books namespace')


@books.route('/<book_name>/<category>/<rent_per_day_range>')
@books.response(404, 'Books not found')
@books.param(name='book_name', description='Book name')
@books.param(name='category', description='Book category name')
@books.param(name='rent_per_day_range', description='Rent range min,max eg. 5,10')
class BooksApi(Resource):
    def get(self, book_name, category, rent_per_day_range):
        '''List all Books'''
        try:
            if rent_per_day_range:
                rent_min, rent_max = map(lambda x: float(x), rent_per_day_range.split(','))
                if rent_min > rent_max:
                    rent_min, rent_max = rent_max, rent_min
            book_list = Book.objects(
                book_name__icontains=book_name,
                category__contains=category,
                rent_per_day__lte = rent_max,
                rent_per_day__gte = rent_min
            )
            return json.loads(book_list.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(500)

