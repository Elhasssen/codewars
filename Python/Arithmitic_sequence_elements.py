def arithmetic_sequence_elements(a, d, n):
    arith = [a]
    for i in range(1,n):
        arith.append(arith[-1] + d)
    # must change element format to string
    # to make join() work proparly
    string = ', '.join(str(v) for v in arith)
    return string