def solution(args):
    theRange = ''
    i = 0
    while i < len(args):
        begin = args[i]
        while i < len(args) - 1 and args[i] + 1 == args[i + 1] :
            i += 1
        end = args[i]
        if end - begin >= 2:
            theRange = theRange + str(begin) + '-' + str(end) + ','
        if end - begin == 1 :
            theRange = theRange + str(begin) + ',' + str(end) + ','
        if end - begin == 0 :
            theRange = theRange + str(begin) + ','
        i += 1
    theRange = theRange[:-1]
    return theRange