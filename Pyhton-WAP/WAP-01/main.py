from book import Book					# Import Class

# Create instances of Book 
b1 = Book('123-456', 'Python Book', 'Alex Johnson', 2024, 'Available')
b2 = Book('456-789', 'JAVA Book', 'Tom Hardy', 2023, 'Borrowed')
b3 = Book('789-123', 'C# Book', 'Jim Willson', 2024, 'Lost')				# Invalid status

# Print attributes of each books
print("ISBN: ", b1.get_isbn())
print("Title: ", b1.get_title())
print("Author: ", b1.get_author())
print("Publish Year: ", b1.get_publish_year())
print("Book Status: ", b1.get_status())

print("\n")
print("ISBN: ", b2.get_isbn())
print("Title: ", b2.get_title())
print("Author: ", b2.get_author())
print("Publish Year: ", b2.get_publish_year())
print("Book Status: ", b2.get_status())

print("\n")
print("ISBN: ", b3.get_isbn())
print("Title: ", b3.get_title())
print("Author: ", b3.get_author())
print("Publish Year: ", b3.get_publish_year())
print("Book Status: ", b3.get_status())
