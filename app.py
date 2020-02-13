import os
import sys
from orm import *

LoadDatabaseBooks()
# object contains all actions user can perform
MainActionObject = {
    "View all books": "1",
    "Add a book": "2",
    "Edit a book": "3",
    "Search for a book": "4",
    "Save and exit": "5",
}

# start-up function that show count of books in db
def StartUp():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        for key, value in MainActionObject.items():
            print(str(value) + ")" + key)
        user_input = input("Choose [1-5]:")
        if user_input in [str(i) for i in range(1, 5)]:
            return
        do_something(user_input)


# this function calls an orm function debending on action
class Strategy:
    def do_logic(self):
        pass


class ListStrategy(Strategy):
    def do_logic(self):
        UserBooksView()


class CreateBookStrategy(Strategy):
    def do_logic(self):
        title = input("Title:")
        author = input("Author:")
        description = input("Description:")
        SaveNewBookToDatabase(title, author, description)


class EditBookStrategy(Strategy):
    def do_logic(self):
        book_id = input(
            "Enter the book ID of the book you want to edit; to return press <Enter>.\nBook ID:"
        )
        if not book_id:
            return
        title = input("Title:")
        author = input("Author:")
        description = input("Description:")
        EditBook(book_id, title, author, description)


class SearchForBookStrategy(Strategy):
    def do_logic(self):
        keyword = input("Search:")
        if not keyword:
            return
        SearchForBook(keyword)


def do_something(action):
    funct_logics = {
        1: ListStrategy,
        2: CreateBookStrategy,
        3: EditBookStrategy,
        4: SearchForBookStrategy,
    }
    startegy = funct_logics.get(action)
    startegy().do_logic()


if __name__ == "__main__":

    print("== BOOK MANAGER ==")
    StartUp()

    # arr = list(map(int, input().rstrip().split()))
