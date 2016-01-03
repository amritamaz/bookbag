import time
import csv
import pdb
import random

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
	    (5) pick a book to read
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
	elif choice == 5:
		session = 'choose'
	elif choice == 0:
		break
	else:
	    print 'oops'

	if session is 'add':
		print "Adding a new book!"
		title = raw_input("What is the title?\n")
		author = raw_input("Who is the author?\n")
		style = raw_input("Fiction or Non-fiction? (N/F)\n")
		gender = raw_input("Non-male author? (Y/N)\n")
		poc = raw_input("POC author? (Y/N)\n")

		if any(((author in k) or (title in k)) for k in to_read):
			for b in to_read:
				if author in b or title in b:
					check = raw_input("Would you like to overwrite "+str(b[0])+" by "+str(b[1])+" (y/n)") 
					if check == 'y':
						to_read.remove(b)
						break


		to_read.append([title,author,gender,poc,style])

	elif session is 'read':
		title = raw_input("What is the title?\n")
		author = raw_input("Who is the author?\n")

		enter_date = raw_input("Did you finish the book today? (y/n)\n")
		date = ''
		if enter_date != 'y' and enter_date != 'Y':
			date = raw_input("When did you finish it? (MM/DD/YYYY)\n")
		else:
			date = time.strftime("%m/%d/%Y")

		pages = raw_input("How many pages?\n")
		gender = raw_input("Non-male author? (Y/N)\n")
		poc = raw_input("POC author? (Y/N)\n")
		difficulty = raw_input("Difficulty? (/5)\n")
		enjoyment = raw_input("Enjoyment? (/5)\n")
		style = raw_input("Fiction or Non-fiction? (N/F)\n")
		genre = raw_input("Genre? \n")
		book_format = raw_input("Format? (book,ebook,etc)\n")


		if any(((author in k) or (title in k)) for k in to_read):
			for b in to_read:
				if author in b or title in b:
					check = raw_input("Would you like to delete "+str(b[0])+" by "+str(b[1])+" (y/n)") 
					if check == 'y':
						to_read.remove(b)
						break

		finished.append([title,author,date,pages,style,genre,book_format,
						difficulty,enjoyment,gender,poc])

	elif session is 'choose':
		filt = raw_input("Would you like to filter your choices? (Y/N)\n")
		if filt == 'Y' or filt == 'y':
			style = raw_input("Fiction (F), Non-fiction (N), or don't care (X)?\n")
			gender = raw_input("Non-male (Y), Male (N), or don't care (X)?\n")
			poc = raw_input("PoC (Y), White (N), or don't care (X)?\n")
		else:
			style = 'X'
			gender = 'X'
			poc = 'X'

		choosing = True
		book = None
		while (choosing):
			book = random.choice(to_read)

			if style != 'X' and book[4] != style:
				continue

			if gender != 'X' and book[2] != gender:
				continue

			if poc != 'X' and book[3] != poc:
				continue

			choosing = False

		print "\n\nYou should try: %s by %s\n\n" % (book[0], book[1])

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
