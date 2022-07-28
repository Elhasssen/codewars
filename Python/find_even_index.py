# You are going to be given an array of integers. 
# Your job is to take that array and find an index 
# N where the sum of the integers to the left of N 
# is equal to the sum of the integers to the right 
# of N. If there is no index that would make this 
# happen, return -1.

import math
def find_even_index(arr):
    even_state = False
    for i in range(0,len(arr)):
        begin = 0
        end = len(arr) 
        right = arr[i+1:end]
        left = arr[begin:i]
        if math.fsum(left) == math.fsum(right):
            if even_state == True :
                break
            even_index = i
            even_state = True
        elif i == len(arr) - 1 and even_state == False :
            even_index = -1
    return even_index