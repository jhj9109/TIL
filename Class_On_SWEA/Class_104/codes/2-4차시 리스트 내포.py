"""
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
"""
data_str ="Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."
data_list = list(data_str)
list1 = list(item for item in data_list if item != 'a')
list2 = list(item for item in list1     if item != 'e')
list3 = list(item for item in list2     if item != 'i')
list4 = list(item for item in list3     if item != 'o')
list5 = list(item for item in list4     if item != 'u')

#print(data_list)
#print(list5)
for i in list5:
    print(i,end="")