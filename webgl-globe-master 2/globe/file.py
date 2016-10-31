import csv
import json

output = ["time"]

f = open( '/Users/nehulyadav/Desktop/all_hour.csv', 'rU' ) 
j = open('file.json', 'w')
for line in f:
    cells = line.split( "," )
output.append( (cells[1], cells[2], cells[3], cells[5] ) )
json.dump(output, j)

