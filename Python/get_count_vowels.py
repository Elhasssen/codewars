def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for elm in sentence:
        if elm in vowels : cnt += 1
    return cnt