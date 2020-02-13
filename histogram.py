import string
from time import time
# A histogram() function which takes a source_text argument (can be either a filename 
# or the contents of the file as a string, your choice) and return a histogram data structure
# that stores each unique word along with the number of times the word appears in the source text.
# A unique_words() function that takes a histogram argument and returns the total count of 
# unique words in the histogram. For example, when given the histogram for 
# The Adventures of Sherlock Holmes, it returns the integer 8475.
# A frequency() function that takes a word and histogram argument 
# and returns the number of times that word appears in a text. For example, 
# when given the word "mystery" and the Holmes histogram, it will return the integer 20.

# What is the least/most frequent word(s)?
# How many different words are used?
# What is the average (mean/median/mode) frequency of words in the text?


# word_histogram = {}

# '''Create function that takes a source text as params and creates a
#  dictionary representing a histogram of words in a list'''
#sample data
# sample_string = 'run love May'

def histogram(lines):
  #empty dictionery
  word_histogram = {}
  #lower casing all words and spliting the from inviduals strings
  for line in lines:
    words = line.rstrip('\n').split()
    for word in words:
      word_count = word_histogram.get(word, 0) + 1
      word_histogram[word] = word_count
      
  
  return word_histogram

def unique_words(word_histogram):
  return len(word_histogram.keys())


# A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text.
def frequency(hist):
# Takes in user input
  user_input = input('enter a word: ')
# If user input not in dictionary raise value error
  if user_input not in hist: raise ValueError('That word is not hist')
# Return value from key
  return hist[user_input]

if __name__ == '__main__':

  filename = "/Users/jarqueviousnelson/Projects/CS-2-Tweet-Generator/source/adamsmith.txt"
  file = open(filename, "r")
  lines = file.readlines()

  hist = histogram(lines)
  print(hist)
  print(unique_words(hist))
  print (frequency(hist))


  



