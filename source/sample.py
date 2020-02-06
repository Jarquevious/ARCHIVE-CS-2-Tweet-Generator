import random
# text = 'one fish two fish red fish blue fish'
# word_counts = {'one': 1, 'fish': 4, 'two': 1,
#                'red': 1, 'blue': 1}
            
def sample_by_frequency(histogram):
    tokens = sum([count for word, count in histogram.items()])
    dart = random.randint(1, tokens)
    fence = 0
    for word, count in histogram.items():
        fence += count
        if fence >= dart:
            return word

# def sample_by_frequency(histogram):
#   # TODO: select a word based on frequency  
#   cum_num = 0 
#   # print(cum_num)
#   print(histogram)
#   sum_values = sum(histogram.values())
#   random_num = random.randint(0, sum_values - 1)
  
#   for k, v in word_counts.items():
#     # print("k:",k)
#     cum_num += v
#     if  cum_num > random_num:
#       return k
#       print(k)
#     else:
#       continue  
#     return k
'''histogram= {}

for i in range(10000):
  word = sample_by_frequency(histogram)
  if word in histogram:
    histogram[word] += 1
  else:
    histogram[word] = 1
  
print(histogram)'''