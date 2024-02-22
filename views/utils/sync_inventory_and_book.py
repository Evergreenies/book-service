from models.book import Book
from models.inventory import Inventory
from models.book_by_attributes import BookByAttributes

from models.database_setup import db


def sync_inventory(book: Book) -> None:
    pass


def sync_book_by_attributes(book: Book) -> None:
    _book = Book.query.filter_by(
        title=book.title, isbn=book.isbn, language=book.language, edition=book.edition
    ).first()
    print(f"sync_book_by_attributes ====> {_book}")

    if _book:
        _update_book_by_language(_book)
        _update_book_by_edition(_book)
        return

    print(f"Book not exist with title: {book.title}")
    return


def _update_book_by_language(book: Book) -> None:
    _book = Book.query.filter_by(title=book.title, language=book.language).count()
    print(f"_update_book_by_language ====> {_book}")
    if _book:
        _book_by_language = BookByAttributes.query.filter_by(
            id=_book.id, attribute="langiage", value=_book.langiage
        )
        if _book_by_language:
            _book_by_language.update({BookByAttributes.count: 0})


def _update_book_by_edition(book: Book) -> None:
    pass
