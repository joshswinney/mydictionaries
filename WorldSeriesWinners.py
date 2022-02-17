#import pprint
import pprint

#open text file
infile = open('WorldSeriesWinners.txt', 'r')

#create dictionary
dictionary1 = {}
dictionary2 = {}

year = 1903

#for loop
for line in infile.readlines():
    dictionary2[year] = line.rstrip()
    year = year + 1
    dictionary1[line.rstrip()] = dictionary1.get(line.rstrip(),0) + 1

#close file
infile.close()

#print dictionary
pprint.pprint(dictionary2)
pprint.pprint(str(dictionary1))
