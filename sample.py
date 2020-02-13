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

  


'''histogram= {}

for i in range(10000):
  word = sample_by_frequency(histogram)
  if word in histogram:
    histogram[word] += 1
  else:
    histogram[word] = 1
  
print(histogram)'''