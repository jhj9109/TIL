"""
다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.
abcdefgabc
"""
data_str="abcdefgabc"

data_dict= {}

for i in data_str: #문자열 1개씩
    cnt=0
    for k in range(0,len(data_str)):
        if i == data_str[k]:
            cnt+=1 #더하고
    data_dict[i]=cnt #입력하고

for key, value in data_dict.items():
    print("{0},{1}".format(key,value))
# print(data_dict)
# print(type(data_dict))