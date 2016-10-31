import urllib, json
urllib.urlretrieve("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv", "all_hour.csv")

text_file = open("places.txt", "w")
text_file2 = open("latitude.txt", "w")
text_file3 = open("longitude.txt", "w")
text_file4 = open("mag.txt", "w")


with open("all_hour.csv") as f:
    lis=[line.split() for line in f]        # create a list of lists
    for i,x in enumerate(lis):              #print the list items
    	text_file.write("line{0} = {1}".format(i,x)["line{0} = {1}".format(i,x).find(',"'):"line{0} = {1}".format(i,x).find('",e')]+ "\n")
    	text_file2.write("line{0} = {1}".format(i,x)["line{0} = {1}".format(i,x).find('0Z,'):"line{0} = {1}".format(i,x).find(',-')]+ "\n")
    	text_file3.write("line{0} = {1}".format(i,x)["line{0} = {1}".format(i,x).find(',-'):"line{0} = {1}".format(i,x).find(',m')]+ "\n")
    	text_file4.write("line{0} = {1}".format(i,x)["line{0} = {1}".format(i,x).find(',1'):"line{0} = {1}".format(i,x).find(',m')]+ "\n")