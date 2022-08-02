

arr = [1,2,3,6,4,1,2,3,2,1]


def pick_peaks(arr):
    dictio = {
        "pos" : [],
        "peaks" : []
    }

    posmax = 0
    is_greater = False
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1] :
            is_greater = True
            posmax = i
        elif arr[i] < arr[i-1] and is_greater:
            is_greater = False
            dictio['pos'].append(posmax)
            dictio['peaks'].append(arr[posmax])
            
    return dictio