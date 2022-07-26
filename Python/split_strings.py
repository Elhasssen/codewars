# Complete the solution so that it splits the string 
# into pairs of two characters. If the string contain
# s an odd number of characters then it should 
# replace the missing second character of the final
#  pair with an underscore ('_').

# Examples:
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
i = 0
s = 'w'
list = []

def solution(s):
    list = []
    if len(s) % 2 != 0 :
        s= s + '_'
    
    for i in range(0,len(s)):
        m = ''
        if i == 0 or i % 2 == 0 : 
            m += s[i] + s[i+1] 
            if len(m) % 2 == 0 :
                list.append(m)
    return list
    
print(solution(s))