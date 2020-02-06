# from time import time
# def timescript():
#     start_time: time.time()
#     s = 0
#     for i in range (1 , n+1):
#         s = s + i

#     end_time = time.time()
#     return s , end_time - start_time
# n = 5
# print(timescript())
# from time import time, ctime
# t = time()
# print(ctime(t))

import timeit

def elapsed_time():
#     code_to_test = """ 
# a = range(100000)
# b = []
# for i in a:
#     b.append(i*2)
#     """
    start_time = 
    end_time = 
    elapsed_time = timeit.timeit(number=100)/100
    print(elapsed_time)
    return elapsed_time


elapsed_time()
    

# also_code_to_test = """
# a = range(100000)
# b = [i*2 for i in a]
# """
# elapsed_time = timeit.timeit(also_code_to_test, number=100)/100
# print(elapsed_time)