#_*_ coding: utf-8 _*_

#맵과 필터를 이용한 실습

data_list=list(range(1,21))
print("{0}".format(data_list))

# map_list = (list((map(lambda x:x+5 ,data_list))))
# filter_list = list((filter(lambda x:x%3==0 ,map_list)))
#
# print("{0}".format(map_list))    #배열 전체에 수행할 계산식은 +5
# print("{0}".format(filter_list))

map_str = input("항목 x에 대해 적용할 표현식을 입력하세요: ")
filter_str = input("항목 x에 적용한 필터를 입력하세요: ")

map_list = list((map(lambda x:eval(map_str) ,data_list)))
filter_list = list((filter(lambda x:eval(filter_str) ,map_list)))

print("{0}".format(map_list))    #배열 전체에 수행할 계산식은 +5
print("{0}".format(filter_list))