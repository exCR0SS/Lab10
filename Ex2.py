import json

def add_book(filename):
    book = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    with open(filename, "r+") as f:
        data = json.load(f)
        new_book = {"book": book, "author": author, "year": year}
        data["books"].append(new_book)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def search_by_author(filename):
    author = input("Enter author name: ")
    with open(filename, "r") as f:
        data = json.load(f)
        found_books = []
        for book in data["books"]:
            if author.lower() == book["author"].lower():
                found_books.append(book)
            if found_books:
                print(f"Books by {author}:")
        for book in found_books:
            print(f'{book["book"]} ({book["year"]})')
        else:
            print(f"No books found by {author}.")

def search_by_year(filename):
    year = input("Enter publication year: ")
    with open(filename, "r") as f:
        data = json.load(f)
        found_books = []
        for book in data["books"]:
            if year == book["year"]:
                found_books.append(book)
            if found_books:
                print(f"Books published in {year}:")
            for book in found_books:
                print(f'{book["book"]} ({book["author"]})')
            else:
                print(f"No books found published in {year}.")

def delete_book(filename):
    book = input("Enter book title: ")
    with open(filename, "r+") as f:
        data = json.load(f)
        for i, b in enumerate(data["books"]):
            if book.lower() == b["book"].lower():
                del data["books"][i]
            break
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

filename = "books.json"

while True:
    print("\nWhat would you like to do?\n1. Add a new book\n2. Search books by author\n3. Search books by year of publication\n4. Delete a book\n5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book(filename)
    elif choice == "2":
        search_by_author(filename)
    elif choice == "3":
        search_by_year(filename)
    elif choice == "4":
        delete_book(filename)
    elif choice == "5":
        break
else:
    print("Invalid choice. Please try again.")