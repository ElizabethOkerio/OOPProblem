from datetime import date

class LibraryBooks(Object):
	def __init__(self,book_name,book_author,book_category):
		self.book_name=book_name
		self.book_author=book_author
		self.book_category=book_category

		class BooksInventory(LibraryBooks):
			def __init__(self,name_of_borrower,date_borrowed,date_returned):
				self.name_of_borrower=name_of_borrower
				self.date_borrowed=date_borrowed
				self.date_returned=date_returned
				tot_books_type=100
			def borrow_book(self,book_name,name_of_borrower,date_borrowed,date_returned):
				if tot_books_type>0:
					tot_books_type-=1
				else:
					return 'Book is not available'
			def return_book(self,book_name,date_returned,name_of_borrower):
				if abs(date_returned-date_borrowed).days>14 days:
					tot_books_type+=1
					return 'Pay fine'
				else:
					return 'No fine'
			def buy_new_books(self,num_of_new_books):
				tot_books_type+=num_of_new_books
			def donate_books(self,num_of_books_to_donate):
				tot_books_type-=num_of_books_to_donate

