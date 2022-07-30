


def valid_parentheses(string):
    queue = []
    para = {    
            '(' : ')'
    }

    if len(string) != 0 : 
        for i in range(len(string)) :
            if string[i] == '(' :
                queue.append(string[i])
            elif para['('] == string[i] and len(queue) == 0:
                return False
            
            elif para['('] == string[i] and len(queue) != 0 :
                queue.pop(len(queue) - 1)
        if len(queue) == 0 :
            return True
        else :
            return False
    else :
        return True
