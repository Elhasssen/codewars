def modify_multiply(st, loc, num):
    words = st.split(' ')
    final = [words[loc]]*num
    return '-'.join(final)