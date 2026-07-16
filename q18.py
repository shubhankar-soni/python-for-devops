with open("bookfairlog", "r") as file:
    lines = file.read().splitlines()

unique_books_read = []
total_books = 0
total_pages = 0
for i in lines:
    line = i.strip()
    parts = line.split(",")
    book_name = parts[1]
    pages = int(parts[2])
    total_pages += pages
    if book_name not in unique_books_read:
        unique_books_read.append(book_name)
    total_books = len(unique_books_read)


print("Total unique books read:", total_books, "and total pages read: ", total_pages)
