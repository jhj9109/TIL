data_list= list(range(1,21))

new_list = [item*item for item in data_list if item%3 or item%5]
print(new_list)