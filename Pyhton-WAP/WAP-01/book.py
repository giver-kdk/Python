class Book:
    book_status_list = ['Available', 'Reserved', 'Borrowed', 'Damaged']

    def __init__(self, isbn, title, author, publish_year, status='Available'):
		# If the status index doesn't lie inside the array
        if status not in self.book_status_list:
            self.status = "Invalid"
        else:
            self.status = status
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publish_year = publish_year

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def get_author(self):  
        return self.author

    def get_publish_year(self):  
        return self.publish_year

    def get_status(self):
        return self.status

    def set_title(self, title_update):
        self.title = title_update
