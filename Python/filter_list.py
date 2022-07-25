def filter_list(l):
    int_list = []
    for elm in l :
        if type(elm) == int :
            int_list.append(elm)
    return int_list

listering = [1,2,'aasf','1','123',123]

print(filter_list(listering))