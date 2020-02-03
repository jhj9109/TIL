# _*_ codimg:utf-8 _*_

#map()

data_list = "abcdef"

result = list(map(lambda x: x.upper(), data_list))

print("{0},{1}".format(type(result),result))