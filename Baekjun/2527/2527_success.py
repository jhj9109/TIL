for _ in range(4):
    A_col1, A_row1, A_col2, A_row2, B_col1, B_row1, B_col2, B_row2 = map(int, input().split())
    result = ''
    if A_col1 > B_col1:
        A_col1, B_col1 = B_col1, A_col1
        A_row1, B_row1 = B_row1, A_row1
        A_col2, B_col2 = B_col2, A_col2
        A_row2, B_row2 = B_row2, A_row2
    if A_col2 < B_col1:
        result = 'd'
    elif A_row2 < B_row1:
        result = 'd'
    elif A_row1 > B_row2:
        result = 'd'
    else:
        result = 'a'
    if A_row2 == B_row1:
        if A_col2 > B_col1:
            result = 'b'
        else:
            result = 'c'
    if A_col2 == B_col1:
        if A_row2 > B_row1:
            result = 'b'
        else:
            result = 'c'
    if B_row2 == A_row1:
        if B_col1 < A_col2:
            result = 'b'
        else:
            result = 'c'
    print(result)