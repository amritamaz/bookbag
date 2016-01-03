import pdb
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
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

<link rel="stylesheet" href="./bootstrap-table.css">

<!-- Latest compiled and minified JavaScript -->
<script src="./bootstrap-table.js"></script>

<style>
body{
  text-transform: capitalize;
}
</style>
</head>
<body>
<div class="container" style="padding:50px;">
<center><h1>Finished Books</h1></center>
<table data-toggle="table" data-sort-name="name" data-sort-order="desc" class="table table-hover table-bordered ">
<thead><tr><th data-sortable="true">#</th><th data-sortable="true">Title</th><th data-sortable="true"> Author</th><th data-sortable="true"> Date<</th><th data-sortable="true"> Pages</th><th data-sortable="true"> Style</th><th data-sortable="true"> Genre</th><th> Format</th><th> Difficulty (/5)</th><th> Enjoyment (/5)</th><th> Non-male?</th><th> POC?</th><th>Cumulative Pages</th></tr></thead>
<tbody>

'''

else:
  header_string = '''
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

<link rel="stylesheet" href="./bootstrap-table.css">

<!-- Latest compiled and minified JavaScript -->
<script src="./bootstrap-table.js"></script>

<style>
body{
  text-transform: capitalize;
}
</style>
</head>
<body>
<div class="container" style="padding:50px;">
<center><h1>Books to Read</h1></center>
<table data-toggle="table"  data-sort-name="name" data-sort-order="desc" class="table table-hover table-bordered ">
<thead><tr><th data-sortable="true">#</th><th data-sortable="true">Title</th><th data-sortable="true"> Author</th><th data-sortable="true"> Fiction?</th><th data-sortable="true"> Non-male?</th><th data-sortable="true"> POC?</th></tr></thead>
<tbody>
'''

footer_string = '''
</tbody>
</table>
</div>
</body>
</html>
'''


with open( sys.argv[ 1 ], 'rU') as csvfile:
    table_string = ""
    reader       = csv.reader( csvfile )
    count = 0
    for row in reader:
        count = count + 1
        # pdb.set_trace()
        table_string += "<tr>" + \
                          "<td>"+str(count)+"</td><td>" + \
                              string.join( row, "</td><td>" ) + \
                          "</td>" + \
                        "</tr>\n"
    
    sys.stdout.write( header_string )
    sys.stdout.write( table_string )
    sys.stdout.write( footer_string )
