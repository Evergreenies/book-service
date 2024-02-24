from werkzeug.routing.converters import UUIDConverter

from twelve_factor_app import app
from views import book

app.app.url_map.converters["uuid"] = UUIDConverter
# book endpoints
app.add_endpoint(
    ["POST", "OPTIONS"], "/books", "create-book-entry", book.create_book_entry
)
app.add_endpoint(["GET"], "/books", "list-all-books", book.list_all_books)
app.add_endpoint(["GET"], "/books/<uuid:book_id>", "book-by-id", book.book_by_id)
app.add_endpoint(["GET"], "/books/search", "search-books", book.search_books)
app.add_endpoint(
    ["PUT"], "/books/<uuid:book_id>", "update-book-by-id", book.update_book_details
)
app.add_endpoint(
    ["DELETE"], "/books/<uuid:book_id>", "delete-book-by-id", book.delete_book
)
