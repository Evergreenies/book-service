from twelve_factor_app_framework.bootstrap import app

from models.book import Book
from models.inventory import Inventory
from models.book_by_attributes import BookByAttributes

from models.database_setup import db, db_engine

# with app.app.app_context():
#    db.create_all()

from routes import book

if __name__ == "__main__":
    with app.app.app_context():
        db.create_all()
    app.run()
