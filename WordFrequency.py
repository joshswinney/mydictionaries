# WordFrequency.py - Write a program that reads the contents of a text file 
# (you can use this file - AI.txt  Download AI.txt). The program should create 
# a dictionary in which the keys are the individual words found in the file and 
# the values are the number of times each word appears. For example, if the word 
# “the” appears 128 times, the dictionary would contain an element with 'the' as 
# the key and 128 as the value. The program should display the frequency of each word.

#import string
import string

#open text file
infile = open('AI.txt', 'r')

#create dictionary
frequency_dict = {}

#For loop
for line in infile:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] = frequency_dict[word] + 1
        else:
            frequency_dict[word] = 1

#close file
infile.close()

#print dictionary
print(frequency_dict)

