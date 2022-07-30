
# Based on the theory of trailing zeroes 
# 

def zeros(n):
    cnt = 0
    pwroffive = 5
    zeroes = 0
    print(n // pwroffive)
    while n > pwroffive : 
        zeroes += n // pwroffive
        pwroffive *= 5
    return zeroes

print(zeros(101))