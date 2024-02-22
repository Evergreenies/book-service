# book-service

## TODO:

### Book Service Endpoints:

Here are some essential endpoints you can implement for the Book Service in your library management system:

**CRUD Operations (Book):**

- **CREATE:** `/books` (POST) - Create a new book entry with details like title, author, ISBN, genre, synopsis, etc.
- **READ:**
  - `/books` (GET) - Retrieve all books in the system with pagination options.
  - `/books/{id}` (GET) - Retrieve details of a specific book by its unique ID.
  - `/books/search` (GET) - Search for books by title, author, ISBN, genre, or keywords.
- **UPDATE:** `/books/{id}` (PUT) - Update details of a specific book based on its ID.
- **DELETE:** `/books/{id}` (DELETE) - Delete a book entry based on its ID.

**CRUD Operations (Inventory):**

- **CREATE:** `/inventory` (POST) - Not recommended, as inventory should be created automatically when adding books.
- **READ:**
  - `/inventory` (GET) - Retrieve all inventory entries (might not be very useful).
  - `/inventory/{id}` (GET) - Retrieve details of a specific inventory entry (useful for specific book copies).
- **UPDATE:** `/inventory/{id}` (PUT) - Update availability or other attributes of a specific inventory entry.
- **DELETE:** `/inventory/{id}` (DELETE) - Remove an inventory entry (use with caution, consider archiving instead).

**Additional Endpoints:**

- `/books/availability` (GET) - Remains unchanged.
- `/books/recommended` (GET) - Remains unchanged.
- `/books/count` (GET) - Now retrieves the total number of books in the system (including unavailable ones).
- `/books/count/{attribute}` (GET) - Retrieve the count of books based on a specific attribute like language or edition (using data from the "Counts" table).
- `/books/search/count` (GET) - Search for books and also return the count of matching results.
- `/inventory/availability/{book_id}` (GET) - Retrieve the number of available copies for a specific book (using data from the "Inventory" table).

**Considerations:**

- Adapt request parameters and response formats to accommodate count information.
- Implement proper authorization for accessing/modifying inventory data.
- Consider caching count data for performance optimization.
- Design endpoints based on your specific use cases and data access needs.

**Bonus:**

- Add endpoints for managing book categories, series, or other metadata.
- Implement filtering and sorting options for search results.
- Integrate with external sources like Google Books API to enrich book information.

### Database representation -

**1. Entity-Relationship Diagram (ERD):**

```
+-----------------+      +-------------------+      +--------------------+
| books           |      | inventory         |      | book_by_attributes |
+-----------------+      +-------------------+      +--------------------+
| id (PK)         |      | id (PK)           |      | id (PK)            |
| title           |      | book_id (FK)      |      | book_id (FK)       |
| author          |      | availability      |      | language           |
| isbn (UNIQUE)   |      | created_at        |      | edition            |
| genre           |      | updated_at        |      | count              |
| synopsis        |      |                   |      | created_at         |
| publication_date|      +-------------------+      | updated_at         |
| publisher       |                                 +--------------------+
| edition         |
| language        |
| pages           |
| format          |
| cover_image_url |
| created_at      |
| updated_at      |
+-----------------+

    1 book can have many copies (1 - M)
    1 book can have many book_by_attributes (1 - M)
```

**2. Table Structure:**

**books table:**

- id (INT, PRIMARY KEY): Unique identifier for the book.
- title (VARCHAR): Title of the book.
- author (VARCHAR): Author(s) of the book.
- isbn (VARCHAR, UNIQUE): International Standard Book Number (optional).
- genre (VARCHAR): Genre(s) of the book.
- synopsis (TEXT): Brief description of the book's content.
- publication_date (DATE): Date of publication.
- publisher (VARCHAR): Publisher of the book.
- edition (VARCHAR): Edition of the book.
- language (VARCHAR): Language of the book.
- pages (INT): Number of pages in the book.
- format (VARCHAR): Format of the book (e.g., paperback, hardcover).
- cover_image_url (VARCHAR): URL of the book's cover image (optional).
- created_at (DATETIME): Timestamp of when the book entry was created.
- updated_at (DATETIME): Timestamp of when the book entry was updated.

**inventory table:**

- id (INT, PRIMARY KEY): Unique identifier for the inventory entry.
- book_id (INT, FOREIGN KEY REFERENCES books(id)): Book this inventory entry belongs to.
- availability (BOOL): Flag indicating if the book is available (true).
- created_at (DATETIME): Timestamp of when the inventory entry was created.
- updated_at (DATETIME): Timestamp of when the inventory entry was updated.
