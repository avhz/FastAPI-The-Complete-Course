from fastapi import Body, FastAPI
from pydantic import BaseModel


app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    category: str


BOOKS = [
    Book(title="Title One", author="Author One", category="science"),
    Book(title="Title Two", author="Author Two", category="science"),
    Book(title="Title Three", author="Author Three", category="history"),
    Book(title="Title Four", author="Author Four", category="math"),
    Book(title="Title Five", author="Author Five", category="math"),
    Book(title="Title Six", author="Author Two", category="math"),
]


def is_equal(a: str, b: str):
    return a.casefold() == b.casefold()


@app.get("/")
async def read_root():
    return {"message": "Server is running"}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{title}")
async def read_book(title: str):
    for book in BOOKS:
        if is_equal(book.title, title):
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    return [b for b in BOOKS if is_equal(b.category, category)]


# Get all books from a specific author using path or query parameters
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    return [b for b in BOOKS if is_equal(b.author, author)]


@app.get("/books/{author}/")
async def read_author_category_by_query(author: str, category: str):
    return [
        book
        for book in BOOKS
        if is_equal(book.author, author) and is_equal(book.category, category)
    ]


@app.post("/books/create_book")
async def create_book(new_book: Book = Body(...)):
    BOOKS.append(new_book)
    return {"message": "Book has been added successfully!", "book": new_book}


@app.put("/books/update_book")
async def update_book(updated_book: Book = Body(...)):
    for book in BOOKS:
        if is_equal(book.title, updated_book.title):
            old_book = book
            book.author = updated_book.author
            book.category = updated_book.category
            return {
                "message": "Book has been updated successfully!",
                "old_book": old_book,
                "new_book": book,
            }


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if is_equal(BOOKS[i].title, book_title):
            BOOKS.pop(i)
            break
