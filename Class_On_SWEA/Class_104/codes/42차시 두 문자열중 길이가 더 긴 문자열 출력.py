def len_check(b):
    if len(b[0])>=len(b[1]):
        print(b[0])
    else:
        print(b[1])

"""
"a,b"문자열 형태로 입력받음
"""

a = input()
a = a.split(', ') #단위로 분류해서 리스트 만들기
len_check(a)

