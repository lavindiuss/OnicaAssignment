import sqlite3 as sq


# this function create a database with all required tables and pass if its already exist
"""
database for : database connection 
database_cursor for : the cursor that controls the structure that enables traversal over the records in the database
"""
database = sq.connect("Books.db")
database_cursor = database.cursor()


def DatabaseCreation():
    database_cursor.execute(
        "CREATE TABLE IF NOT EXISTS Book(id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(200),author VARCHAR(255),description VARCHAR(500))"
    )


DatabaseCreation()


# this function loads and return a list of db books
"""
books_list for : list of books that shows the output of books query 
"""


def LoadDatabaseBooks():
    try:
        books_list = database_cursor.execute("SELECT * FROM Book").fetchall()
        print("--" + str(len(books_list)) + " BOOKS LOADED INTO THE LIBRARY--\n")
        return books_list
    except Exception as e:
        print(str(e))


# this function list the ids and the titles of each book , and also returns a book details if it got a book id
"""
list_of_ids_and_titles for : list contains all ids and titles of books 
book_details for : tuple contains particular book data 
"""


def UserBooksView(book_id=None,is_edit=False):
    list_of_ids_and_titles = database_cursor.execute(
        "SELECT id,title FROM Book"
    ).fetchall()
    if book_id != None:
        book_details = database_cursor.execute(
            "SELECT * FROM Book WHERE id = {}".format(book_id)
        ).fetchone()
        if not is_edit:
            print("ID:{}\n Title:{} \n Author:{} \n Description:{}".format(book_details[0],book_details[1],book_details[2],book_details[3]))
        else:
            return book_details
    else:
            
        for book in list_of_ids_and_titles:
            #TODO
            print("[{}] {}".format(book[0],book[1]))


# this function takes the id of a book and partial update its attributes
"""
data_to_edit for : list contains all book data we can edit
"""


def EditBook(book_id=None, title=None, author=None, description=None):
    data_to_edit = [title, author, description, book_id]
    database_cursor.execute(
        "UPDATE Book SET title= ?,author= ?,description= ? WHERE id= ?", data_to_edit
    )
    database.commit()
    print("--Book edited successfully--")


# this function takes new book required attributes and save it to database
"""
data_to_save for : list of data that contains new book details
"""


def SaveNewBookToDatabase(title=None, author=None, description=None):
    data_to_save = [title, author, description]
    database_cursor.execute(
        "INSERT INTO Book(title,author,description) VALUES (?,?,?)", data_to_save
    )
    database.commit()
    print("--Book saved successfully--")


# this function takes keyword from user and search in database within it
"""
result for : attribute contains search resutl
"""


def SearchForBook(keyword=None):
    result = database_cursor.execute(
        "SELECT * FROM Book WHERE title like '%{}%'".format(keyword)
    ).fetchall()
    print("The following books matched your query. Enter the book ID to see more details, or <Enter> to return.")
    for book in result:
        print("[{}] {} ".format(book[0],book[1]))


UserBooksView(2)