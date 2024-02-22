from twelve_factor_app_framework.bootstrap import app
from views import book


# book endpoints
app.add_endpoint(
    ["POST", "OPTIONS"], "/book", "create-book-entry", book.create_book_entry
)
