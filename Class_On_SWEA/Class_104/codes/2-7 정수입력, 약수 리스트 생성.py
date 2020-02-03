num = int(input())
data_list=[]
for i in range(1,num+1):
    if num%i ==0:
        data_list.append(i)
print(data_list)