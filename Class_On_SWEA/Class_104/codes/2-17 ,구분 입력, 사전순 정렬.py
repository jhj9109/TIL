"""
단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
"""

a=list(input().split(', '))
a_sorted = sorted(a)
k=1
for i in a_sorted:
    if k == (len(a)):
        print(i)
    else:
        print(i, end=", ")
    k+=1
print("")