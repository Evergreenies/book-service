from typing import Any, Dict
from models.book import Book
from models.inventory import Inventory
from models.book_by_attributes import BookByAttributes

from models.database_setup import db, session_maker


def sync_inventory(book: Book) -> None:
    pass


def sync_book_by_attributes(book: Book) -> None:
    _book = None
    with session_maker() as session:
        _book = (
            session.query(Book)
            .filter_by(
                title=book.title,
                isbn=book.isbn,
                language=book.language,
                edition=book.edition,
            )
            .first()
        )
        print(f"sync_book_by_attributes ====> {_book}")

        if _book:
            _update_book_by_language(_book)
            _update_book_by_edition(_book)

    print(f"Book not exist with title: {book.title}")
    return


def _update_book_by_language(book: Book) -> None:
    with session_maker() as session:
        _book_count = (
            session.query(Book)
            .filter_by(title=book.title, language=book.language)
            .count()
        )

        print(f"_update_book_by_language ====> {_book_count}")
        if _book_count:
            with session_maker() as session:
                _book_by_language = session.query(BookByAttributes).filter_by(
                    id=book.id, attribute="language", value=book.language
                )
                if _book_by_language:
                    _book_by_language.update({BookByAttributes.count: _book_count})
                    session.add(_book_by_language)
                else:
                    _book_by_attribute = BookByAttributes(
                        book_id=book.id,
                        attribute="language",
                        value=book.language,
                        count=_book_count,
                    )
                    session.add(_book_by_attribute)

                    session.commit()


def _update_book_by_edition(book: Book) -> None:
    pass
