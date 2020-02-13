from random import randint
import sys 
# from time_script import elapsed_time
import time


def rearrange(lines):
  start_time = time.time()
  #lines = ['brown', 'cow', 'how']

  for i in range(len(lines)):
    ran_index = randint(0, len(lines)-1)
    #randint start with lower bound and and ends with upper bound. 
    # in this case upperbound is subtracted from 1 because we read it from 1,2,3 
    #but the computer reads it from 0,1,2

    lines[i],lines[ran_index] = lines[ran_index],lines[i]
    #swapping index i with random index
  elapsed_time = time.time() - start_time
  print("Total Time:", elapsed_time)
  print(lines)


if __name__ == "__main__":
    sentence = " ".join(sys.argv[1:]).split(" ")
    rearrange(sentence)

