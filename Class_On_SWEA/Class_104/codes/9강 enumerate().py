data_list = range(10,60,10)

for idx, val in enumerate(data_list):
    print("{0}:{1}".format(idx,val))

print("-"*25)

for obj in enumerate(data_list):
    print("{0}:{1}".format(obj[0], obj[1]))

print("-"*25)

for obj in enumerate(data_list):
    print("{0}:{1}".format(*obj))