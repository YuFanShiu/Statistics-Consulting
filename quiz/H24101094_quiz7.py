library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """
    book_info = input("Enter the title, genre, and price of the book separated by vertical bars (|): ")
    try:
        title, genre, price = book_info.split('|')
        price = float(price)
        library[title.strip()] = (genre.strip(), price)
        print(f'\nAdded"{title.strip()}" to the library.')
        return True
    except ValueError:
        print("\nInvalid input. Please enter the details in the correct format: title|genre|price")
        return False

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    title = input("Enter the title of the book to remove: ").strip()
    if title in library:
        del library[title]
        print(f'\nRemoved "{title}" from the library.')
        return True
    else:
        print(f'\nBook "{title}" not found in the library.')
        return False

def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """
    title = input("Enter the title of the book: ").strip()
    if title in library:
        genre, price = library[title]
        print(f'\nTitle: {title}\nGenre: {genre}\nPrice: ${price:.2f}')
    else:
        print(f'\nBook "{title}" not found in the library.')

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print(f"{title} ({genre}, ${price:.2f})")
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    genre_search = input("Enter the genre to search for: ").strip()
    found_books = {title: info for title, info in library.items() if info[0].lower() == genre_search.lower()}
    
    if not found_books:
        print(f'\nNo books found in the "{genre_search}" genre.')
        return False
    print()
    for title, (genre, price) in sorted(found_books.items()):
        print(f'{title} (Q, ${price:.2f})')
    print()
    return True

while True:
    print("\nMenu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")
