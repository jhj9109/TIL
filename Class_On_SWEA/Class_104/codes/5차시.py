gugu_list=[]
list1 = list(range(1,10))
list2 = list(range(2,10))
for i in list2: #2~9
    temp = []
    for k in list1: #10
        if (i*k)%3 !=0 :
            if (i*k)%7 !=0 :
                temp.append(i * k)
    gugu_list.append(temp)
print(gugu_list)