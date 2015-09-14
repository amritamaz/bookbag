
import sys
import os
import csv
import string

if len( sys.argv ) < 2 :
    sys.stderr.write( sys.argv[ 0 ]  + 
                      ": usage - "   + 
                      sys.argv[ 0 ]  + " [.csv file name]\n" )
    sys.exit()

if not os.path.exists(sys.argv[ 1 ]):
    sys.stderr.write( sys.argv[ 1 ] + " not found \n" )
    sys.exit()

if 'finished' in sys.argv[1]:
  header_string = '''
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<style>
body{
  text-transform: capitalize;
}
</style>
</head>
<body>
<div class="container" style="padding:50px;">
<center><h1>Finished Books</h1></center>
<table class="table table-hover table-bordered ">
<tr><th>Title</th><th> Author</th><th> Date<</th><th> Pages</th><th> Style</th><th> Genre</th><th> Format</th><th> Difficulty (/5)</th><th> Enjoyment (/5)</th><th> Non-male?</th><th> POC?</th></tr>

'''

else:
  header_string = '''
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<style>
body{
  text-transform: capitalize;
}
</style>
</head>
<body>
<div class="container" style="padding:50px;">
<center><h1>Books to Read</h1></center>
<table class="table table-hover table-bordered ">
<tr><th>Title</th><th> Author</th><th> Style</th><th> Non-male?</th><th> POC?</th></tr>

'''

# header_string = '''
# <html>
# <head>
# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

# <!-- Optional theme -->
# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

# <!-- Latest compiled and minified JavaScript -->
# <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
# <style>
# body{
#   text-transform: capitalize;
# }
# </style>
# </head>
# <body>
# <div class="container" style="padding:50px;">
# <center><h1>Finished Books</h1></center>
# <table class="table table-hover table-bordered ">
# <tr><th>Title</th><th> Author</th><th> Date<</th><th> Pages</th><th> Style</th><th> Genre</th><th> Format</th><th> Difficulty (/5)</th><th> Enjoyment (/5)</th><th> Non-male?</th><th> POC?</th></tr>

# '''

footer_string = '''
</table>
</div>
</body>
</html>
'''


with open( sys.argv[ 1 ], 'rb') as csvfile:
    table_string = ""
    reader       = csv.reader( csvfile )
    
    for row in reader:
        table_string += "<tr>" + \
                          "<td>" + \
                              string.join( row, "</td><td>" ) + \
                          "</td>" + \
                        "</tr>\n"
    
    sys.stdout.write( header_string )
    sys.stdout.write( table_string )
    sys.stdout.write( footer_string )