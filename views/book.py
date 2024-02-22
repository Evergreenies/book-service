from flask import jsonify, request

from models.book import Book

from views.utils.sync_inventory_and_book import sync_inventory, sync_book_by_attributes

from models.database_setup import db


def create_book_entry():
    try:
        print("POST CALL TO STORE ENTRIES IN DATABASE")
        data = request.get_json()
        _book = Book(**data)
        db.session.add(_book)
        db.session.commit()

        sync_book_by_attributes(_book)
        sync_inventory(_book)

        print(data, _book, _book.id)
        return data, 200
    except Exception as ex:
        print(ex)
        return "Error", 500
