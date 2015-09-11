import time
import csv
import pdb

finished = []
to_read = []

to_read_csv = 'to_read.csv'
finished_csv = 'finished.csv'

# format: Title,Author,non-male,POC?,style (f/nf)
with open(to_read_csv, 'rb') as f:
    reader = csv.reader(f)
    to_read = list(reader)
    f.close()

#format: 
# Title, Author, Date Completed, Pages,
# Style, Genre, Format, Difficulty (/5), Enjoyment (/5), non-male (y/n), poc (y/n)
with open(finished_csv, 'rb') as f:
    reader = csv.reader(f)
    finished = list(reader)
    f.close()

choice = -1

while choice != 0:
	print """Welcome to BookBot (tm)! You can: 
	    (1) add a book to the to-read pile
	    (2) add/move a book to the finished pile
	    (3) see the list of finished books
	    (4) see the list of books to read
	    (0) exit
	    Enter the number for your choice."""

	choice = input()
	session = ''

	if choice == 1:
	    session = 'add'
	elif choice == 2:
	    session = 'read'
	elif choice == 3:
		session = 'print-done'
	elif choice == 4:
		session = 'print-to-read'
	elif choice == 0:
		break
	else:
	    print 'oops'

	if session is 'add':
		print "Adding a new book!"
		title = input("What is the title?\n")
		author = input("Who is the author?\n")
		style = input("Fiction or Non-fiction? (N/F)\n")
		gender = input("Non-male author? (Y/N)\n")
		poc = input("POC author? (Y/N)\n")

		to_read.append([title,author,gender,poc,style])

	elif session is 'read':
		title = input("What is the title?\n")
		author = input("Who is the author?\n")

		enter_date = input("Did you finish the book today? (y/n)\n")
		date = ''
		if enter_date != 'y' and enter_date != 'Y':
			date = input("When did you finish it? (MM/DD/YYYY)\n")
		else:
			date = time.strftime("%m/%d/%Y")

		pages = input("How many pages?\n")
		gender = input("Non-male author? (Y/N)\n")
		poc = input("POC author? (Y/N)\n")
		difficulty = input("Difficulty? (/5)\n")
		style = input("Fiction or Non-fiction? (N/F)\n")
		enjoyment = input("Enjoyment? (/5)\n")
		difficulty = input("Difficulty? (/5)\n")
		genre = input("Genre? \n")
		book_format = input("Format? (book,ebook,etc)\n")


		if any(((author in k) and (title in k)) for k in to_read):
			# find where it is in to_read and delete it

		finished.append([title,author,date,pages,style,genre,book_format,
						difficulty,enjoyment,gender,poc])

	else:
		print 'Sorry! not supported yet. '

	with open(finished_csv, 'wb') as f:
		wr = csv.writer(f, dialect='excel')
		wr.writerows(finished)
		f.close()

	with open(to_read_csv, 'wb') as f:
		wr = csv.writer(f, dialect='excel')
		wr.writerows(to_read)
		f.close()

print('bye!')
