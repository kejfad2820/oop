class Book:
	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year

class Library:
	def __init__(self):
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def remove_book(self, title):
		for book in self.books:
			if book.title == title:
				self.books.remove(book)
				return 1
			else:
				return 0

	def find_book(self, title):
		for book in self.books:
			if book.title == title:
				return book
			else:
				return 0
library = Library()

book1 = Book("1984", "Morgan", "1984")
book2 = Book("1534", "Janson", "2005")
book3 = Book("666", "Lucifer", "1966")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

found_book = library.find_book(book1.title)
if found_book:
	print(f"title = {found_book.title}\nAuthor = {found_book.author}")
else:
	print("Not founded")

removed_book = library.remove_book(book1.title)
if removed_book:
	print(f"{book1.title} is deleted from library")
else:
	print("NOt")

found_book = library.find_book(book1.title)
if found_book:
	print(f"title = {found_book.title}\nAuthor = {found_book.author}")
else:
	print("Not founded")
