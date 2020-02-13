import os
import sys
from orm import *
from straegy import *


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
        if user_input not in [str(i) for i in range(1, 6)]:
            continue
        if user_input =="5":
            print("Library Saved")
            break
        do_something(user_input)


# this function calls an orm function debending on action

def do_something(action):
    funct_logics = {
        "1": ListStrategy,
        "2": CreateBookStrategy,
        "3": EditBookStrategy,
        "4": SearchForBookStrategy,
        "5": ExitStrategy
    }
    startegy = funct_logics.get(action)
    startegy().do_logic()


if __name__ == "__main__":

    print("== BOOK MANAGER ==")
    StartUp()

    # arr = list(map(int, input().rstrip().split()))
