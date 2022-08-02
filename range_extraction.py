theList = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

theRange = ''
theMiniRange = [theList[0]]
begin = 0

for i in range(1,len(theList)):
    if theList[begin] + 1 == theList[i]:
        theMiniRange.append(theList[i])
        begin = i
        
    else :
        if len(theMiniRange) != 1 :
            theRange = theRange + str(theMiniRange[0]) + '-' + str(theMiniRange[-1]) + ','
            begin = i
            theMiniRange = [theList[i]]
        elif len(theMiniRange) == 1 :
            theRange = theRange + str(theMiniRange[0]) + ','
            begin = i
            theMiniRange = [theList[i]]
    print(f'the begin is {begin}')
    print(f'the i value is {i}')
    print(theMiniRange)
    print(theRange)

