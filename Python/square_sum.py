def square_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += pow(numbers[i],2)
    return sum
    #your code here