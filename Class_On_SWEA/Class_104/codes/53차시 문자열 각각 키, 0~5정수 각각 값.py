data_str="abcdef"
data_int=list(range(6))

data_list=list(data_str)
data_dict={}
for i in range(6) :
    data_dict[data_list[i]] = data_int[i]
    print("{0}: {1}".format(data_list[i], data_int[i]))

#print (data_dict)
#
# for i in data_dict:
#     print("{0}: {1}".format(i,data_dict[i]))
#     # print (data_dict)
#data_dict[data_list[0]]=data_int[0]