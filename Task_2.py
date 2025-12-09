size_mb = 1.44
str = 100
lines = 50
chars_per_line = 25
bytes_per_char = 4

book_chars = str * lines * chars_per_line
book_bytes = book_chars * bytes_per_char
floppy_bytes = size_mb * 1024 * 1024
books_count = int(floppy_bytes / book_bytes)

print("Количество книг, помещающихся на дискету:", books_count)
