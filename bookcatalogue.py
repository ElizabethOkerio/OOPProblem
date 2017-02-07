class SchoolLibraryCatalogue(Object):

def __init__(self,name_of_book,author_of_book,book_category):

	self.name_of_book = name_of_book
	self.author_of_book = author_of_book
	self.book_category = book_category
	number_of_books_of_that_category = 100


def borrow_book(self,name_of_book,date_borrowed,name_of_borrower):

	if number_of_books_of_that_category>0:

		number_of_books_of_that_category-=1;

		date_borrowed = date_borrowed

		name_of_borrower = name_of_borrower

	else:

		return 'Book is not available at the moment! Check back later'

def retun_book(self,name_of_book,date_returned,name_of_returnee):

     if name_of_returnee == name_of_borrower:

     	number_of_books_of_that_category+=1;

     	date_returned = date_returned

     	name_of_returnee = name_of_returnee


     else:

     	return 'Special Case'

def buy_new_books(self,num_of_new_books):

	number_of_books_of_that_category+=num_of_new_books

def donate_books(self,num_of_books_to_donate):

	number_of_books_of_that_category -=num_of_books_to_donate;

	














