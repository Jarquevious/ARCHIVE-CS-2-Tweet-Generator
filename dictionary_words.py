from random import randint, sample
# from time_script import elapsed_time
#open and read the file
my_file = open("/usr/share/dict/words", "r")
words = my_file.readlines()

# print (words)

#get a random word from list
new_list = []
read_ran_word = randint(3, 6)
ran_words = sample(words, read_ran_word)
for i in range(len(ran_words)):
    new_list.append(ran_words[i])


new_list = " ".join(new_list)
list2 = ""
for _ in range(len(new_list)):
    new_list.strip("\n")
    list2 = list2 + new_list[_]

new_list = new_list.replace("\n", "")
print(new_list)
a = "/source/dictionary_words.py"

# elapsed_time()

