
# # https://brilliant.org/wiki/finding-the-last-digit-of-a-power/
# we can recognise patterns after various powers are in dictionary above,
# ex : 1 : [1 power of 1, 1 power of 2, 1 power of 3,power of 4....and so on]
# The set of last digits of powers forms a periodic sequence with periods given 
# by the table below:
# Digit     Period
# ------------------
# 0,1,5,6 |  1
# 2,3,7,8 |  4
# 4,9     |  2

def last_digit(n1,n2):
    if n2 == 0:
        return 1
    else : 
        #w
        last_digit_n1 = int(str(n1)[-1])
        
        cycle_of_onenum = cycles[last_digit_n1]
        return cycle[(n2 % 4) - 1]


# def last_digit(n1, n2):
#     return pow( n1, n2, 10 )