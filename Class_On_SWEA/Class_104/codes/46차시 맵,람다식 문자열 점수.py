"""
"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.
"""

# for i in b:
#     k = 0
#     if a[0]== i: k += 1
#     if a[1]== i: k += 1
#     print(k, end=" ")

data = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
data_list = list(data) #문자열을 리스트 변환
result=0
for i in data_list:
    if i == "A" : result+=4
    elif i == "B" : result+=3
    elif i == "C":   result +=2
    elif i == "D": result +=1

print(result)