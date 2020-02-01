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


# filename = "adamsmith.txt"
# lines = open(filename, "r")
# word_histogram = {}

# '''Create function that takes a source text as params and creates a dictionary representing a histogram of words in a list'''
sample_string = 'run love May'

def histogram(sample_string):
  word_histogram = {}
  words = sample_string.split()
  for word in words:
    print(word)
  #TODO: add code to increase the count in the histogram for the given word
    if word not in word_histogram:
      word_histogram[word]=1
    else:
      word_histogram[word]+= 1
  return word_histogram

def unique_words(word_histogram):
  return len(word_histogram.keys())
  
def frequency(hist):
  user_input = input('enter a word: ')
  return hist[user_input]


hist = histogram(sample_string)
print(hist)
print(unique_words(hist))
print (frequency(hist))


      

# def unique_word():
#   num_of_keys = 0
#   keys_in_words_histogram = word_histogram.keys()
#   for i in keys_in_words_histogram:
#     num_of_keys =+ 1
#   return num_of_keys
#   print(num_of_keys)


# def frequency():
#   user_input = input("enter a word")


  
# print(histogram())
# # print(" ")

# sample_string = ['run', 'love', 'May']
# def histogram():
#   word_dictionary = {}
#   words = sample_string.split()


  
  # for word in sample_string:
  #   if word in word_dictionary:
  #     word_dictionary[word] += 1
  #   else:
  #     word_dictionary[word] = 1
  # for key in 
