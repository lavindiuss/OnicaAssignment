from orm import *

class Strategy:
    def do_logic(self):
        pass


class ListStrategy(Strategy):
    def do_logic(self):
        UserBooksView()
        _next = input("To view details enter the book ID, to return press <Enter>.")
        if _next:     
            UserBooksView(int(_next))
            input("to return press <Enter>")

            

class CreateBookStrategy(Strategy):
    def do_logic(self):
        title = input("Title:")
        author = input("Author:")
        description = input("Description:")
        SaveNewBookToDatabase(title, author, description)
        input("to return press <Enter>")


class EditBookStrategy(Strategy):
    def do_logic(self):
        UserBooksView()
        book_id = input(
            "Enter the book ID of the book you want to edit; to return press <Enter>.\nBook ID:"
        )
        if not book_id:
            return
        book_details = UserBooksView(int(book_id),True)
        title = input("Title [{}]:".format(book_details[0]))
        author = input("Author [{}]:".format(book_details[1]))
        description = input("Description [{}]:".format(book_details[2]))
        EditBook(book_id, title, author, description)
        input("to return press <Enter>")


class SearchForBookStrategy(Strategy):
    def do_logic(self):
        print("Type in one or more keywords to search for")
        keyword = input("Search:")
        if not keyword:
            return
        SearchForBook(keyword)
        _next = input("Book ID:")
        if _next:
            UserBooksView(int(_next))
            input("to return press <Enter>")
        else:
            return
