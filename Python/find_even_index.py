import math


arr = list(range(1,100))




   
# for i in range(0,len(arr)):
#     print(f'--------i = {i}')
#     print(f'array is  {arr}')
#     index = i
#     print(f'index is  {index}')
#     begin = 0
#     print(f'begin  is  {begin}')
#     end = len(arr) 
#     print(f'end is  {end}')
#     right = arr[i+1:end]
#     print(f'right list is {right}')
#     print(f'math.fsum of right list is {int(math.fsum(right))}')
#     left = arr[begin:i]
#     print(f'left list is {left}')
#     print(f'math.fsum of left list is {math.fsum(left)}')
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

print(even_index)