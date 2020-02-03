# _*_ coding:utf-8 _*_

#자료형인자 변환하는 함수

data_str = "Hello"

data_list = list(data_str)
print("{0},{1},{2}".format(data_str,type(data_list),data_list))

data_tuple = tuple(data_list)
print("{0},{1},{2}".format(data_str,type(data_tuple),data_tuple))

data_set = set(data_list)
print("{0},{1},{2}".format(data_tuple, type(data_set),data_set))

data_dict = dict(enumerate(data_set))
print("{0},{1},{2}".format(data_set,type(data_dict),data_dict))