data_list = [3,8,12,2,5,11]

asc_result = sorted(data_list)

print("{0},{1}".format(type(data_list),data_list))
print("{0},{1}".format(type(asc_result),asc_result))

print("-"*35)

desc_result = list (reversed(asc_result))

print("{0},{1}".format(type(data_list),data_list))
print("{0},{1}".format(type(asc_result),asc_result))
print("{0},{1}".format(type(desc_result),desc_result))
