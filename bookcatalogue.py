from datetime import date

class SchoolLibraryBooks(Object):

def __init__(self,name_of_book,author_of_book,book_category):

	self.name_of_book = name_of_book
	self.author_of_book = author_of_book
	self.book_category = book_category


	class IssueandBorrowBooks(SchoolLibraryBooks):

		name_of_book = SchoolLibraryBooks.name_of_book

		def __init__(self,name_of_borrower,date_borrowed,date_returned):

			self.name_of_borrower = name_of_borrower
			self.date_borrowed = date_borrowed
			self.date_returned = date_returned
			number_of_books_of_that_category = 100


       def borrow_book(self,name_of_book,date_borrowed,name_of_borrower):

        if number_of_books_of_that_category>0:

        	number_of_books_of_that_category-=1:

        else:

        	return 'Book is not available'


        def retun_book(self,name_of_book,date_returned,name_of_borrower):

        	if abs(date_returned-date_borrowed).days > 14 days:

        		number_of_books_of_that_category+=1

        		return 'Pay fine'

        	else:

        		return 'No fine'


        def buy_new_books(self,num_of_new_books):

	        number_of_books_of_that_category+=num_of_new_books

        def donate_books(self,num_of_books_to_donate):

	        number_of_books_of_that_category-=num_of_books_to_donate;
















