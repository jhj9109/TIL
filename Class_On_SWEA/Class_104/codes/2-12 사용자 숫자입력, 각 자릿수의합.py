"""
사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.
예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.
"""
data_list=list(input())
result=0
for i in data_list:
    result+=int(i)
print(result)
