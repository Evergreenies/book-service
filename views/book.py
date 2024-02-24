from urllib.parse import urldefrag
from marshmallow.fields import Bool
from psycopg2.errors import InvalidTextRepresentation
from flask import jsonify, request
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import DataError

from twelve_factor_app_framework.bootstrap import app

from models.book import Book, BookSchema
from models.database_setup import session_maker

logger = app.logger


def create_book_entry():
    try:
        data = request.get_json()

        with session_maker() as session:
            _book = Book(
                title=data.get("title"),
                isbn=data.get("isbn"),
                genre=data.get("genre"),
                auther=data.get("auther"),
                language=data.get("language"),
                edition=data.get("edition"),
                format=data.get("format"),
                pages=data.get("pages"),
                synopsis=data.get("synopsis"),
                publication_date=data.get("publication_date"),
                cover_image_url=data.get("cover_image_url"),
                publisher=data.get("publisher"),
            )
            session.add(_book)
            session.commit()

            logger.info("Book detailes stored successfully.")
        return "Book details stored successfully.", 200
    except Exception:
        logger.error("while preserving book details.", exc_info=True)
        return "Some error while preserving book details.", 501


def list_all_books():
    try:
        with session_maker() as session:
            return BookSchema(many=True).dumps(session.query(Book).all())
    except Exception:
        logger.error("while fetching all books details.", exc_info=True)
        return "Trouble to fetch books details.", 500


def book_by_id(book_id: UUID):
    if not book_id:
        return "Invalid book uuid", 404
    try:
        with session_maker() as session:
            book = session.query(Book).get(book_id)
            if not book:
                return f"Book not found with the uuid you provided: {book_id}", 404
            return BookSchema(many=False).dumps(book), 200
    except DataError:
        logger.error(f"Invalid book_id: {book_id}", exc_info=True)
        return f"Invalid book_id: {book_id}", 404
    except Exception:
        logger.error(f"while fetching book: {book_id} details", exc_info=True)
        return "Seme error while fetching book details.", 500


def update_book_details(book_id: UUID):
    try:
        with session_maker() as session:
            book = session.query(Book).get(book_id)
            if not book:
                return f"Book: {book_id} not found", 404

            book_schema = BookSchema().dump(book)
            data = request.get_json()

            for key in book_schema.keys():
                if key == "id":
                    continue
                value = data.get(key)
                if value is None:
                    continue

                if key in ["auther", "edition"]:
                    velue = ", ".join(value)

                setattr(book, key, value)

            session.commit()
            session.flush()

            return f"Book: {book_id} details has been updated.", 200
    except DataError:
        logger.error(f"Invalid book_id: {book_id}", exc_info=True)
        return f"Invalid book_id: {book_id}", 404
    except Exception:
        logger.error(f"while updating book: {book_id}", exc_info=True)
        return "Some error while updating book details.", 500


def delete_book(book_id: UUID):
    try:
        with session_maker() as session:
            book = session.query(Book).get(book_id)
            if not book:
                return f"Book with id: {book_id} does not exists.", 404

            session.delete(book)
            session.commit()

        return f"Book with id {book_id} is deleted.", 200
    except DataError:
        logger.error(f"Invalid book_id: {book_id}", exc_info=True)
        return f"Invalid book_id: {book_id}", 404
    except Exception:
        logger.error(f"while deleting book: {book_id}", exc_info=True)
        return f"Some execption while deleting book: {book_id}", 500


def search_books():
    try:
        with session_maker() as session:
            filters = request.args.to_dict()
            query = session.query(Book)

            for attriburte, value in filters.items():
                if hasattr(Book, attriburte):
                    if isinstance(value, list):
                        query = query.filter(getattr(Book, attriburte).in_(value))
                    else:
                        query = query.filter(getattr(Book, attriburte) == value)

            return BookSchema(many=True).dumps(query.all())
    except DataError:
        logger.error("Invalid book_id provided.", exc_info=True)
        return "Invalid book_id provided.", 404
    except Exception:
        logger.error("while seaching books.", exc_info=True)
        return "Some error while seaching books.", 500
