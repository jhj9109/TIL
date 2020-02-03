def filtering(data):
    data_set = set(data)
    return list(data_set)       #ret_list = list(data_set)

data_list=[1,2,3,4,3,2,1]

print(data_list)
print("{0}".format(filtering(data_list)))